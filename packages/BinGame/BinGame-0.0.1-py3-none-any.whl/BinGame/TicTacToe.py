from PIL import Image, ImageDraw


class TicTacToe:

    def __init__(self):
        self.image = self._new_image()
        self.item = {
            '1': (0, 0),
            '2': (1, 0),
            '3': (2, 0),
            '4': (0, 1),
            '5': (1, 1),
            '6': (2, 1),
            '7': (0, 2),
            '8': (1, 2),
            '9': (2, 2)
        }
        self.records = {'True': [], 'False': [], "index": 0}
        self.result = [
            [1, 2, 3, 0],
            [4, 5, 6, 0],
            [7, 8, 9, 0],
            [1, 4, 7, 1],
            [2, 5, 8, 1],
            [3, 6, 9, 1],
            [1, 5, 9, 2],
            [3, 5, 7, 3]
        ]

    @staticmethod
    def _new_image():
        """ 创建新的棋盘图片 """
        # 创建 120 * 120 的空白图片
        image = Image.new('RGB', (120, 120), (255, 255, 255))

        # 创建画笔
        draw = ImageDraw.Draw(image, image.mode)

        # 开始画线
        for i in range(1, 3):
            start = i * 40

            draw.line(((0, start), (120, start)), fill='black')
            draw.line(((start, 0), (start, 120)), fill='black')

        return image

    def play(self, records: dict, index: str, camp: bool):
        """
        下棋
        :param records: 记录集
        :param index: 索引
        :param camp: True ⚪, False X
        :return: tuple[image, int], 如果0 则 胜利, 1 则 继续, 2 则平局
        """
        index = int(index)
        if not (1 <= index <= 9):
            raise Exception('非法坐标, 坐标越界')

        # 判断目标位置是否存在棋子
        if index in records['True'] or index in records['False']:
            raise Exception('非法坐标, 坐标位置上已经存在棋子.')

        records[str(camp)].append(index)
        records['index'] += 1

        # 渲染
        image, draw = self.rendering(records)

        return image, self.win(records, camp, draw)

    def win(self, records: dict, camp: bool, draw: ImageDraw):
        """
        判断胜负
        :param records: 记录集
        :param camp: 阵营
        :param draw 画笔
        :return 0 胜利, 1 继续, 2 平局
        """

        # 棋盘上少于 5 枚棋子 不可以能分出胜负
        if records['index'] < 5:
            print('===')
            return 1

        r = False
        camp = str(camp)
        for result in self.result:
            piece_list = records[camp]
            print(piece_list, '[[[[', result)
            if result[0] in piece_list and result[1] in piece_list and result[2] in piece_list:
                start_x, start_y = self.item[str(result[0])]
                end_x, end_y = self.item[str(result[2])]

                if result[3] == 1:
                    draw.line(((start_x * 40 + 20, start_y * 40), (end_x * 40 + 20, end_y * 40 + 40)), fill="red",
                              width=2)
                elif result[3] == 0:
                    draw.line(((start_x * 40, start_y * 40 + 20), (end_x * 40 + 40, end_y * 40 + 20)), fill="red",
                              width=2)
                elif result[3] == 2:
                    print('--=-=-=')
                    draw.line(((start_x * 40, start_y * 40), (end_x * 40 + 40, end_y * 40 + 40)), fill="red",
                              width=2)
                elif result[3] == 3:
                    draw.line(((start_x * 40 + 40, start_y * 40), (end_x * 40, end_y * 40 + 40)), fill="red",
                              width=2)

                r = True

        if r:
            return 0

        if records['index'] == 9:
            return 2

        return 1

    def rendering(self, records: dict):
        """
        渲染棋盘
        :param records: 记录集
        :return: image
        """
        image = self.image.copy()
        draw = ImageDraw.Draw(image, image.mode)

        for index in records['True']:
            x, y = self.item[str(index)]
            start_x = x * 40 + 5
            start_y = y * 40 + 5
            draw.ellipse(((start_x, start_y), (start_x + 30, start_y + 30)), outline='red', width=3)

        for index in records['False']:
            x, y = self.item[str(index)]
            print(x, y)
            start_x = x * 40 + 5
            start_y = y * 40 + 5
            draw.line(((start_x, start_y), (start_x + 30, start_y + 30)), fill="black", width=3)
            draw.line(((start_x + 30, start_y), (start_x, start_y + 30)), fill="black", width=3)

        return image, draw
