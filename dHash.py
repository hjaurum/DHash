class DHash(object):
    @staticmethod
    def calculate_hash(image):
        """
        计算图片的dHash值
        :param image: PIL.Image
        :return: dHash值,string类型
        """
        difference = DHash.__difference(image)
        # 转化为16进制(每个差值为一个bit,每8bit转为一个16进制)
        decimal_value = 0
        hash_string = ""
        for index, value in enumerate(difference):
            if value:  # value为0, 不用计算, 程序优化
                decimal_value += value * (2 ** (index % 8))
            if index % 8 == 7:  # 每8位的结束
                hash_string += str(hex(decimal_value)[2:].rjust(2, "0"))  # 不足2位以0填充。0xf=>0x0f
                decimal_value = 0
        return hash_string

    @staticmethod
    def hamming_distance(first, second):
        """
        计算两张图片的汉明距离(基于dHash算法)
        :param first: Image或者dHash值(str)
        :param second: Image或者dHash值(str)
        :return: hamming distance. 值越大,说明两张图片差别越大,反之,则说明越相似
        """
        # A. dHash值计算汉明距离
        if isinstance(first, str):
            return DHash.__hamming_distance_with_hash(first, second)

        # B. image计算汉明距离
        hamming_distance = 0
        image1_difference = DHash.__difference(first)
        image2_difference = DHash.__difference(second)
        for index, img1_pix in enumerate(image1_difference):
            img2_pix = image2_difference[index]
            if img1_pix != img2_pix:
                hamming_distance += 1
        return hamming_distance

    @staticmethod
    def __difference(image):
        """
        *Private method*
        计算image的像素差值
        :param image: PIL.Image
        :return: 差值数组。0、1组成
        """
        resize_width = 9
        resize_height = 8
        # 1. resize to (9,8)
        smaller_image = image.resize((resize_width, resize_height))
        # 2. 灰度化 Grayscale
        grayscale_image = smaller_image.convert("L")
        # 3. 比较相邻像素
        pixels = list(grayscale_image.getdata())
        difference = []
        for row in range(resize_height):
            row_start_index = row * resize_width
            for col in range(resize_width - 1):
                left_pixel_index = row_start_index + col
                difference.append(pixels[left_pixel_index] > pixels[left_pixel_index + 1])
        return difference

    @staticmethod
    def __hamming_distance_with_hash(dhash1, dhash2):
        """
        *Private method*
        根据dHash值计算hamming distance
        :param dhash1: str
        :param dhash2: str
        :return: 汉明距离(int)
        """
        difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
        return bin(difference).count("1")

