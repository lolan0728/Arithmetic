# & *********************************************
# & @Date: 2023-05-04 13:39:53
# & @LastEditors: lolan0728 vampire.lolan@outlook.com
# & @LastEditTime: 2023-05-11 16:37:05
# & @FilePath: /Arithmetic/IO/SettingLoader.py
# & @Description: 設定ファイルから情報読込
# & *********************************************
import hjson
import os


class SettingLoader:

    # ロジッククラス
    MAKER_FILE = {'FILE': 'LogicClasses.hjson', 'BLOCK': 'QuestionsMaker'}
    # テンプレート定義ファイル
    TEMPLATE_FILE = {'FILE': 'Templates.hjson', 'BLOCK': 'Templates'}
    # Factor定義ファイル
    FACTOR_FILE = {'FILE': 'Factors.hjson', 'BLOCK': 'Factors'}

    # *********************************************
    # * @description: 数式作成クラス情報読込
    # * @return {list[str]}: クラス情報のリスト
    # *********************************************
    @classmethod
    def loadMakerClasses(cls) -> list[str]:
        try:
            # パス
            path = os.path.join('Settings', cls.MAKER_FILE['FILE'])
            # ブロック
            block = cls.MAKER_FILE['BLOCK']
            return cls.loadHJSON(path, block)
        except Exception:
            raise

    # *********************************************
    # * @description: テンプレート定義ファイル読込
    # * @return {list}: テンプレート情報
    # *********************************************
    @classmethod
    def loadTemplates(cls) -> list:
        try:
            # パス
            path = os.path.join('Settings', cls.TEMPLATE_FILE['FILE'])
            # ブロック
            block = cls.TEMPLATE_FILE['BLOCK']
            return cls.loadHJSON(path, block)
        except Exception:
            raise

    # *********************************************
    # * @description: Factor定義ファイル読込
    # * @return {list}: Factor情報
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

    # *********************************************
    # * @description: hjson(json)ファイルから情報読込
    # * @param {str} path: ファイルのパス
    # * @param {str} block:　ブロック
    # * @return {list[str]}:　情報リスト
    # *********************************************
    @classmethod
    def loadHJSON(cls, path: str, block: str) -> list[str]:
        try:
            with open(path) as j:
                return hjson.load(j)[block]
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
