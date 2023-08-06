"""Single table diagnostic report."""

import copy
import itertools
import pickle
import sys
import warnings

import numpy as np
import pandas as pd
import pkg_resources
import tqdm

from sdmetrics.errors import IncomputableMetricError
from sdmetrics.single_table import BoundaryAdherence, NewRowSynthesis, RangeCoverage


RESULT_DETAILS = {
    'BoundaryAdherence': {
        'SUCCESS': (
            '✓ The synthetic data general follows the min/max boundaries set by the real data'
        ),
        'WARNING': (
            '! More than 10% the synthetic data does not follow the min/max boundaries set by '
            'the real data'
        ),
        'DANGER': (
            'x More than 50% the synthetic data does not follow the min/max boundaries set by '
            'the real data'
        ),
    }
    'NewRowSynthesis': {
        'SUCCESS': '✓ The synthetic rows are generally not copies of the real data',
        'WARNING': '! More than 10% of the synthetic rows are copies of the real data',
        'DANGER': 'x More than 50% of the synthetic rows are copies of the real data',
    },
    'RangeCoverage': {
        'SUCCESS': (
            '✓ The synthetic data generally covers numerical ranges present in the real data'
        ),
        'WARNING': (
            '! The synthetic data is missing more than 10% of the numerical ranges present in '
            'the real data'
        ),
        'DANGER': (
            'x The synthetic data is missing more than 50% of the numerical ranges present in '
            'the real data'
        ),
    }
}


class DiagnosticReport():
    """Single table diagnostic report.

    This class creates a diagnostic report for single-table data. It calculates the diagnostic
    score along three properties - synthesis, coverage, and boundaries.
    """

    METRICS = [BoundaryAdherence, NewRowSynthesis, RangeCoverage]

    def __init__(self):
        self._metric_results = {}
        self._metric_scores = {}
        self._metric_errors = {}

    def _print_results(self, out=sys.stdout):
        """Print the diagnostic report results."""
        success_metrics = []
        warning_metrics = []
        danger_metrics = []
        for metric, score in self._metric_scores.items():
            if np.isnan(score):
                continue
            if score >= 0.9:
                success_metrics.append(metric.__name__)
            elif score >= 0.5:
                warning_metrics.append(metric.__name__)
            else:
                danger_metrics.append(metric.__name__)

        if len(success_metrics) > 0:
            print('SUCCESS:\n')
            for metric in success_metrics:
                print(f'{RESULT_DETAILS[metric]}')

        if len(warning_metrics) > 0:
            print('WARNING:\n')
            for metric in warning_metrics:
                print(f'{RESULT_DETAILS[metric]}')

        if len(danger_metrics) > 0:
            print('DANGER:\n')
            for metric in warning_metrics:
                print(f'{RESULT_DETAILS[metric]}')

    def generate(self, real_data, synthetic_data, metadata):
        """Generate report.

        Args:
            real_data (pandas.DataFrame):
                The real data.
            synthetic_data (pandas.DataFrame):
                The synthetic data.
            metadata (dict):
                The metadata, which contains each column's data type as well as relationships.
        """
        for metric in tqdm.tqdm(self.METRICS, desc='Creating report'):
            metric_name = metric.__name__
            try:
                self._metric_results[metric_name] = metric.compute_breakdown(
                    real_data, synthetic_data, metadata)
            except IncomputableMetricError:
                # Metric is not compatible with this dataset.
                self._metric_results[metric_name] = {}

        for metric in metrics:
            avg_score, num_metric_errors = aggregate_metric_results(
                self._metric_results[metric_name])

            self._metric_scores[metric_name] = avg_score
            self._metric_errors[prop] = num_prop_errors

        self._overall_quality_score = np.nanmean(list(self._metric_scores.values()))

        self._print_results()

    def get_score(self):
        """Return the overall diagnostic score.

        Returns:
            float
                The overall diagnostic score.
        """
        return self._overall_quality_score

    def get_properties(self):
        """Return the property score breakdown.

        Returns:
            pandas.DataFrame
                The property score breakdown.
        """
        return copy.deepcopy(self._metric_scores)

    def get_visualization(self, property_name):
        """Return a visualization for each score for the given property name.

        Args:
            property_name (str):
                The name of the property to return score details for.

        Returns:
            plotly.graph_objects._figure.Figure
                The visualization for the requested property.
        """
        pass

    def get_details(self, property_name):
        """Return the details for each score for the given property name.

        Args:
            property_name (str):
                The name of the property to return score details for.

        Returns:
            pandas.DataFrame
                The score breakdown.
        """
        columns = []
        metrics = []
        scores = []
        errors = []
        details = pd.DataFrame()

        if property_name == 'New Row Synthesis':
            details = pd.DataFrame({
                'Metric': property_name,
                'Quality Score': self._metric_scores[property_name],
            })

        else:
            for column, score_breakdown in self._metric_results[metric.__name__].items():
                columns.append(column)
                metrics.append(metric.__name__)
                scores.append(score_breakdown.get('score', np.nan))
                real_scores.append(score_breakdown.get('real', np.nan))
                synthetic_scores.append(score_breakdown.get('synthetic', np.nan))
                errors.append(score_breakdown.get('error', np.nan))

            details = pd.DataFrame({
                'Column 1': [col1 for col1, _ in columns],
                'Column 2': [col2 for _, col2 in columns],
                'Metric': metrics,
                'Quality Score': scores,
                'Real Correlation': real_scores,
                'Synthetic Correlation': synthetic_scores,
            })

        if pd.Series(errors).notna().sum() > 0:
            details['Error'] = errors

        return details

    def get_raw_result(self, metric_name):
        """Return the raw result of the given metric name.

        Args:
            metric_name (str):
                The name of the desired metric.

        Returns:
            dict
                The raw results
        """
        metrics = list(itertools.chain.from_iterable(self.METRICS.values()))
        for metric in metrics:
            if metric.__name__ == metric_name:
                return [
                    {
                        'metric': {
                            'method': f'{metric.__module__}.{metric.__name__}',
                            'parameters': {},
                        },
                        'results': {
                            key: result for key, result in
                            self._metric_results[metric_name].items()
                            if not np.isnan(result.get('score', np.nan))
                        },
                    },
                ]

    def save(self, filepath):
        """Save this report instance to the given path using pickle.

        Args:
            filepath (str):
                The path to the file where the report instance will be serialized.
        """
        self._package_version = pkg_resources.get_distribution('sdmetrics').version

        with open(filepath, 'wb') as output:
            pickle.dump(self, output)

    @classmethod
    def load(cls, filepath):
        """Load a ``QualityReport`` instance from a given path.

        Args:
            filepath (str):
                The path to the file where the report is stored.

        Returns:
            QualityReort:
                The loaded diagnostic report instance.
        """
        current_version = pkg_resources.get_distribution('sdmetrics').version

        with open(filepath, 'rb') as f:
            report = pickle.load(f)
            if current_version != report._package_version:
                warnings.warn(
                    f'The report was created using SDMetrics version `{report._package_version}` '
                    f'but you are currently using version `{current_version}`. '
                    'Some features may not work as intended.')

            return report
