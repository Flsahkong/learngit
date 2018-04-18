# coding=utf-8

class ProvinceList:
    def __init__(self):
        self.province = {
            '0000': '全国',
            '1100': '北京市',
            '1200': '天津市',
            '1300': '河北省',
            '1400': '山西省',
            '1500': '内蒙古自治区',
            '2100': '辽宁省',
            '2200': '吉林省',
            '2300': '黑龙江省',
            '3100': '上海市',
            '3200': '江苏省',
            '3300': '浙江省',
            '3400': '安徽省',
            '3500': '福建省',
            '3600': '江西省',
            '3700': '山东省',
            '4100': '河南省',
            '4200': '湖北省',
            '4300': '湖南省',
            '4400': '广东省',
            '4500': '广西壮族自治区',
            '4600': '海南省',
            '5000': '重庆市',
            '5100': '四川省',
            '5200': '贵州省',
            '5300': '云南省',
            '5400': '西藏自治区',
            '6100': '陕西省',
            '6200': '甘肃省',
            '6300': '青海省',
            '6400': '宁夏回族自治区',
            '6500': '新疆维吾尔自治区',
            '7100': '台湾省',
            '8100': '香港特别行政区',
            '8200': '澳门特别行政区'
        }

        self.proDaiHao = {
            '0000': '全国',
            '1100': '京',
            '1200': '津',
            '1300': '冀',
            '1400': '晋',
            '1500': '蒙',
            '2100': '辽',
            '2200': '吉',
            '2300': '黑',
            '3100': '沪',
            '3200': '苏',
            '3300': '浙',
            '3400': '皖',
            '3500': '闽',
            '3600': '赣',
            '3700': '鲁',
            '4100': '豫',
            '4200': '鄂',
            '4300': '湘',
            '4400': '粤',
            '4500': '桂',
            '4600': '琼',
            '5000': '渝',
            '5100': '川',
            '5200': '贵',
            '5300': '云',
            '5400': '藏',
            '6100': '陕',
            '6200': '甘',
            '6300': '青',
            '6400': '宁',
            '6500': '新',
        }

    def CodeToProvince(self, code):
        return self.province.get(code, 'error')

    def CodeToProDaiHao(self,code):
        return self.proDaiHao.get(code,'error')