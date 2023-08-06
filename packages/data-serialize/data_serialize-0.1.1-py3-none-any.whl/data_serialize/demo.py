#
import data_serialize


def test_feature():
    val1 = data_serialize.Int64List(value =[1,2,3] * 20)
    val2 = data_serialize.FloatList(value =[1,2,3] * 20)
    val3 = data_serialize.BytesList(value = [b'The china', b'boy'])

    featrue = data_serialize.Features(feature=
        {
            "item_0": data_serialize.Feature(int64_list = val1),
            "item_1": data_serialize.Feature(float_list = val2),
            "item_2": data_serialize.Feature(bytes_list = val3)
        }
    )

    example = data_serialize.Example(features=featrue)

    serialize = example.SerializeToString()
    print(serialize)

    #parse
    example = data_serialize.Example()
    example.ParseFromString(serialize)
    print(example)

test_feature()






