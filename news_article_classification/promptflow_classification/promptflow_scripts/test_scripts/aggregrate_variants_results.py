from typing import List
from promptflow import tool, log_metric
import numpy as np

@tool
def aggregate_variants_results(variant_id: List[int], line_number: List[int], results: List[dict]):
    aggregate_results = {}
    for index in range(len(line_number)):
        result = results[index]
        variant = variant_id[index]
        if variant not in aggregate_results.keys():
            aggregate_results[variant] = {}
        item_result = aggregate_results[variant]
        for name, value in result.items():
            if name not in item_result.keys():
                item_result[name] = []
            try:
                float_val = float(value)
            except Exception:
                float_val = np.nan
            item_result[name].append(float_val)

    for name, value in aggregate_results.items():
        variant_id = name
        aggr_item = aggregate_results[name]
        for name, value in aggr_item.items():
            metric_name = name
            aggr_item[name] = np.nanmean(value)
            if 'pass_rate' in metric_name:
                metric_name = metric_name + "(%)"
                aggr_item[name] = aggr_item[name] * 100.0
            aggr_item[name] = round(aggr_item[name], 2)
            log_metric(metric_name, aggr_item[name], variant_id=variant_id)

    return aggregate_results


