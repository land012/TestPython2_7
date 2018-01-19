#!/home/opt/python2.7.5/bin/python
# -*- coding:utf-8 -*-
import sys
import struct
import ujson as json
from common_pb2 import FULLY_RELIABLE
from sample_pb2 import Sample, ContentFeature
import ctr_int_key_reduce_pb2
import ctr_str_key_reduce_pb2

reload(sys)
sys.setdefaultencoding('utf-8')

def bistreaming_input():
    data = sys.stdin.read(4)
    while data:
        size, = struct.unpack('<i', data)
        key = sys.stdin.read(size)
        if len(key) != size:
            raise Exception
        size, = struct.unpack('<i', sys.stdin.read(4))
        value = sys.stdin.read(size)
        if len(value) != size:
            raise Exception
        yield key, value
        data = sys.stdin.read(4)


def bistreaming_emit(key, value):
    sys.stdout.write(struct.pack('<i', len(key)))
    sys.stdout.write(key)
    sys.stdout.write(struct.pack('<i', len(value)))
    sys.stdout.write(value)


def read_ctr_dict(ctr_dict):
    # url词典
    ctr_url_infos = ctr_int_key_reduce_pb2.CtrInfoes()
    f = open('ctr_url_link', 'rb')
    ctr_url_infos.ParseFromString(f.read())
    f.close()

    url_dict = {}
    for ctr_info in ctr_url_infos.ctrinfo:
        detail_list = []
        detail_list.append(ctr_info.click)
        detail_list.append(ctr_info.show)
        detail_list.append(ctr_info.ctr)
        url_dict[ctr_info.rid] = detail_list
    ctr_url_infos = None
    ctr_dict['url'] = url_dict

    # tag词典
    ctr_tag_infos = ctr_str_key_reduce_pb2.CtrInfoes()
    f = open('ctr_tag_link', 'rb')
    ctr_tag_infos.ParseFromString(f.read())
    f.close()

    tag_dict = {}
    for ctr_info in ctr_tag_infos.ctrinfo:
        tag_dict[str(ctr_info.key)] = ctr_info.ctr
    ctr_tag_infos = None
    ctr_dict['tag'] = tag_dict

    # attention词典
    ctr_att_infos = ctr_str_key_reduce_pb2.CtrInfoes()
    f = open('ctr_att_link', 'rb')
    ctr_att_infos.ParseFromString(f.read())
    f.close()

    att_dict = {}
    for ctr_info in ctr_att_infos.ctrinfo:
        att_dict[str(ctr_info.key)] = ctr_info.ctr
    ctr_att_infos = None
    ctr_dict['att'] = att_dict

    # domain词典
    ctr_domain_infos = ctr_str_key_reduce_pb2.CtrInfoes()
    f = open('ctr_domain_link', 'rb')
    ctr_domain_infos.ParseFromString(f.read())
    f.close()

    domain_dict = {}
    for ctr_info in ctr_domain_infos.ctrinfo:
        domain_dict[str(ctr_info.key)] = ctr_info.ctr
    ctr_domain_infos = None
    ctr_dict['domain'] = domain_dict


def read_idf_dict(idf_dict):
    with open('idf_utf8_link') as f:
        for line in f:
            (key, val) = line.strip().split('\t')
            idf_dict[key] = float(val)


def content_model_2_feature(feature, model, ctr_dict={}, idf_dict={}):
    feature.Clear()
    # 目前都是必须字段，没有就异常，不做验证
    nid = long(model['nid'])
    feature.nid = nid
    feature.title = str(model['title'])

    for img_id in model['img_ids']:
        picture_hash = feature.picture_hash.add()
        picture_hash.low = img_id if img_id < 9223372036854775808L \
            else -(18446744073709551616L - img_id)

    for tj_tag in model['tj_tags']:
        tag = feature.tag.add()
        tag_name = str(tj_tag[0])
        tag.name = tag_name
        # 添加idf值
        if tag_name in idf_dict:
            tag.idf = float(idf_dict[tag_name])
        # score赋值
        tag.score = float(tj_tag[1])
        product_ctr = tag.product_ctr.add()
        tag_ctr = ctr_dict.get('tag').get(tag_name)
        if tag_ctr is not None:
            product_ctr.value = float(tag_ctr)

    for news_attention, score in model['news_attention'].iteritems():
        attention = feature.attention.add()
        attention_name = str(news_attention)
        attention.name = attention_name
        # 添加idf值
        if attention_name in idf_dict:
            attention.idf = float(idf_dict[attention_name])

        # score赋值
        attention.score = float(score)
        product_ctr = attention.product_ctr.add()
        att_ctr = ctr_dict.get('att').get(attention_name)
        if att_ctr is not None:
            product_ctr.value = float(att_ctr)

    category = feature.category
    category.name = str(model['news_category'])
    category.score = float(model['news_category_prob'])

    sub_category = feature.sub_category
    sub_category.name = str(model['news_sub_category'])
    sub_category.score = float(model['news_sub_category_prob'])

    feature.picture_num = int(model['img_num'])

    sub_dict_url = ctr_dict.get('url').get(nid)

    if sub_dict_url is not None:
        if sub_dict_url[0] is not None:
            click = sub_dict_url[0]
            product_click_num = feature.product_click_num.add()
            product_click_num.value = long(click)

        if sub_dict_url[1] is not None:
            show = sub_dict_url[1]
            product_show_num = feature.product_show_num.add()
            product_show_num.value = long(show)

        if sub_dict_url[2] is not None:
            ctr = sub_dict_url[2]
            product_ctr = feature.product_ctr.add()
            product_ctr.value = float(ctr)

    site = str(model['site'])
    domain_ctr = ctr_dict.get('domain').get(site)
    if domain_ctr is not None:
        product_domain_ctr = feature.product_domain_ctr.add()
        product_domain_ctr.value = float(domain_ctr)

    # tod: comment_num = 15;
    # tod: mark_num = 16;
    # tod: share_num = 17;
    feature.domain = site
    feature.source_id = int(model['source_id'])
    feature.mthid = str(model['mthid'])
    feature.quality = int(model['quality_score']['final_score'])

    # authority = 22;
    # complete_ratio = 23;
    # duration = 24;
    # vulgar = 25;

    feature.publish_timestamp = long(model['public_time'])
    feature.url = str(model['url'])
    feature.rencency = int(model['tj_timeliness'])

    quality_influence = model.get('quality_influence')
    if quality_influence is not None:
        feature.quality_influence = float(quality_influence)
    feature.author_activity_score = float(model['author_activity_score'])
    feature.author_authority_score = int(model['author_authority_score'])
    feature.author_quality_score = float(model['author_quality_score'])

    nlpc_title_seg = model.get('nlpc_title_seg')
    if nlpc_title_seg is not None:
        feature.title_seg.extend(map(str, model['nlpc_title_seg']))
        feature.title_seg_available = True
    feature.title_seg_available = True

    nlpc_title_ner = model.get('nlpc_title_ner')
    if nlpc_title_ner is not None:
        feature.title_ner.extend(map(str, model['nlpc_title_ner']))
        feature.title_ner_available = True
    feature.title_ner_available = True

    feature.vertical_type = int(model['vertical_type'])

    resolution = model.get('resolution')
    if resolution is not None:
        feature.image_set_resolution = int(resolution)

    news_location_level = model.get('news_location_level')
    if news_location_level is not None:
        feature.news_location_level = int(news_location_level)

    # locnames = model.get('locname')
    # if locnames and locnames[0]:
    #     locname = locnames[0]
    #     location = feature.location.add()
    #     province = locname.get('province')
    #     if province is not None and \
    #             isinstance(province[0], basestring):
    #         location.province = province[0]
    #     city = locname.get('city')
    #     if city is not None and \
    #             isinstance(city[0], basestring):
    #         location.city = city[0]
    #     district = locname.get('district')
    #     if district is not None and \
    #             isinstance(district[0], basestring):
    #         location.district = district[0]
    #     if circle is not None and \
    #             isinstance(circle[0], basestring):
    #         location.circle = circle[0]

    # feature.copy_level = int(model['copy_level'])
    # feature.copy_time = int(model['copy_time'])
    # feature.ad_level = int(model['ad_level'])
    # feature.disgust_level = int(model['disgust_level'])
    # feature.disgust_score = float(model['disgust_score'])
    # feature.news_clickbait_level = int(model['news_clickbait_level'])
    # feature.news_clickbait_score = float(model['news_clickbait_score'])
    # feature.quality_feature_level = int(model['quality_feature_level'])
    # feature.quality_feature_score = float(model['quality_feature_score'])
    # feature.old_news_level = int(model['old_news_level'])
    # feature.high_timeliness = int(model['high_timeliness'])
    # feature.site_name = str(model['site_name'])
    # feature.low_matching_level = int(model['low_matching_level'])
    # feature.low_matching_score = float(model['low_matching_score'])

    feature.reliability_level = FULLY_RELIABLE

ctr_dict = {}
read_ctr_dict(ctr_dict)

idf_dict = {}
read_idf_dict(idf_dict)

sample = Sample()
content_feature = sample.context.add().content_feature


def output(value):
    model = json.loads(value)
    try:
        content_model_2_feature(content_feature, model, ctr_dict, idf_dict)
    except:
        sys.stderr.write('error data = %s' % value)
        return

    data = sample.SerializeToString()
    size = struct.pack('>i', len(data))
    sys.stdout.write(size)
    sys.stdout.write(data)


last_nid = None
last_value = None
for key, value in bistreaming_input():
    nid, timestamp = key.split('\t')
    if nid != last_nid:
        if last_nid is not None:
            output(last_value)
        last_nid = nid
    last_value = value
if last_nid is not None:
    output(last_value)
