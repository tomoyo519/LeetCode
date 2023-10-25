class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 반복문 말고 방법있음..?
        result = []
        min_len = min(strs, key=len)
        # 0,1,2,
        flag = False;
        for i in range(len(min_len)):
            first_idx = min_len[i]
            if(flag):
                break;
            for j in range(len(strs)):
                if(strs[j][i]== first_idx and j == len(strs)-1):
                    result.append(strs[j][i]);
                elif(strs[j][i]== first_idx):
                    continue;
                elif(strs[j][i]!= first_idx):
                    flag = True;
                    break;

        # # 0,1,2,
        # for i in range(len(strs)):
        #     # 0,1,2,3
            
        #     for j in range(len(min_len)):
        #         first_idx = min_len[j];
        #         if(strs[i][j] == first_idx and j == len(min_len) -1 ):
        #             result.append(first_idx);
        #         elif(strs[i][j] == first_idx and j < len(min_len) -1):
        #             continue;
        #         elif(strs[i][j] != first_idx):
        #             break;
        return ''.join(result)
