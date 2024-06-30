class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list_dict = [
            {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'},
            {0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'},
            {0:'',1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'},
            {0:'',1:'M',2:'MM',3:'MMM'}
        ]
        result = ''
        index = 0
        while num != 0:
            result = list_dict[index][num % 10] + result
            index += 1
            num = num // 10 
        return result
