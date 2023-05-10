# *********************************************
# * @Date: 2023-05-04 13:39:53
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-09 16:51:21
# * @FilePath: /Arithmetic/IO/SettingLoader.py
# * @Description: Settingファイルを読み込む
# *********************************************
import hjson
import os


class SettingLoader:

    # 数式作成クラス
    MAKER_FILE = {'FILE': 'LogicClasses.hjson', 'BLOCK': 'QuestionsMaker'}
    #
    TEMPLATE_FILE = {'FILE': 'Templates.hjson', 'BLOCK': 'Templates'}
    #
    FACTOR_FILE = {'FILE': 'Factors.hjson', 'BLOCK': 'Factors'}

    # *********************************************
    # * @description: hjson(json)ファイルから情報読込
    # * @param {str} path: ファイルのパス
    # * @param {str} block:　情報塊
    # * @return {*}:　読み込んだ情報のリスト
    # * @Date: 2023-05-04 17:14:38
    # *********************************************
    @classmethod
    def loadHJSON(cls, path: str, block: str) -> list:
        try:
            with open(path) as j:
                return hjson.load(j)[block]
        except Exception:
            raise

    # *********************************************
    # * @description: 数式作成クラス情報読込
    # * @return {*}: クラス情報のリスト
    # * @Date: 2023-05-04 20:39:33
    # *********************************************
    @classmethod
    def loadMakerClasses(cls) -> list:
        try:
            # ファイルのパス
            path = os.path.join('Settings', cls.MAKER_FILE['FILE'])
            # 情報ブロック
            block = cls.MAKER_FILE['BLOCK']
            return cls.loadHJSON(path, block)
        except Exception:
            raise

    # *********************************************
    # * @description:
    # * @param {*} cls
    # * @return {*}
    # * @Date: 2023-05-09 11:15:36
    # *********************************************
    @classmethod
    def loadTemplates(cls) -> list:
        try:
            # ファイルのパス
            path = os.path.join('Settings', cls.TEMPLATE_FILE['FILE'])
            # 情報ブロック
            block = cls.TEMPLATE_FILE['BLOCK']
            return cls.loadHJSON(path, block)
        except Exception:
            raise

    # *********************************************
    # * @description:
    # * @param {*} cls
    # * @return {*}
    # * @Date: 2023-05-09 11:15:36
    # *********************************************
    @classmethod
    def loadFactors(cls) -> list:
        try:
            # ファイルのパス
            path = os.path.join('Settings', cls.FACTOR_FILE['FILE'])
            # 情報ブロック
            block = cls.FACTOR_FILE['BLOCK']
            return cls.loadHJSON(path, block)
        except Exception:
            raise


# テスト用
if __name__ == '__main__':
    # from Definition.Template import Template
    from Entity.Factors import Factor, FactorCollection
    try:
        lst = SettingLoader.loadFactors()
        coll = FactorCollection()
        coll.setFactors([Factor(**item) for item in lst])
        f = coll.getFactorByName('mixed1')
        print(f.name)
    except Exception as e:
        print('error!!!!', e)
