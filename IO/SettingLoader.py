# *********************************************
# * @Date: 2023-05-04 13:39:53
# * @LastEditors: lolan0728 vampire.lolan@outlook.com
# * @LastEditTime: 2023-05-06 16:24:28
# * @FilePath: /Arithmetic/IO/SettingLoader.py
# * @Description: Settingファイルを読み込む
# *********************************************
import hjson


class SettingLoader:

    # 数式作成クラス
    MAKER_CLASSES = {
        'PATH': 'Settings/LogicClasses.hjson',
        'BLOCK': 'QuestionsMaker'
    }

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
            path = cls.MAKER_CLASSES['PATH']
            # 情報塊
            block = cls.MAKER_CLASSES['BLOCK']
            return cls.loadHJSON(path, block)
        except Exception:
            raise


# テスト用
if __name__ == '__main__':
    try:
        dic = SettingLoader.loadMakerClasses()
        for item in dic:
            print(item["name"])
    except Exception as e:
        print('error!!!!', e)
