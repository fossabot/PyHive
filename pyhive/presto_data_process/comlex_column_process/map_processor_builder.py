from pyhive.presto_data_process.comlex_column_process.complex_cell_processor_builder import \
    PrestoComplexCellProcessorBuilder
from pyhive.presto_data_process.comlex_column_process.map_processor import PrestoMapProcessor


class PrestoMapProcessorBuilder(PrestoComplexCellProcessorBuilder):
    def extract_inner_type_signatures(self, column_type_signature):
        return [column_type_signature.get("arguments")[1].get("value")]

    def build_cell_processor(self, column_type_signature, inner_column_processors):
        key_primitive_type = _extract_key_primitive_type(column_type_signature)

        return PrestoMapProcessor(inner_column_processors[0], key_primitive_type)


def _extract_key_primitive_type(column_type_signature):
    return column_type_signature.get('arguments')[0].get('value').get('rawType')
