from .muxing import Muxing


class FMP4Muxing(Muxing):

    def __init__(self, streams, segment_length, segment_naming=None, init_segment_name=None, outputs=None, id_=None,
                 custom_data=None):

        super().__init__(id_=id_, custom_data=custom_data, streams=streams, outputs=outputs)
        self.segmentLength = segment_length
        self.segmentNaming = segment_naming
        self.initSegmentName = init_segment_name

    @classmethod
    def parse_from_json_object(cls, json_object):
        muxing = super().parse_from_json_object(json_object=json_object)
        id_ = muxing.id
        custom_data = muxing.customData
        streams = muxing.streams
        outputs = muxing.outputs
        segment_length = json_object['segmentLength']
        segment_naming = json_object.get('segmentNaming')
        init_segment_name = json_object.get('initSegmentName')

        fmp4_muxing = FMP4Muxing(streams=streams, segment_length=segment_length, segment_naming=segment_naming,
                                 init_segment_name=init_segment_name, outputs=outputs, id_=id_, custom_data=custom_data)

        return fmp4_muxing
