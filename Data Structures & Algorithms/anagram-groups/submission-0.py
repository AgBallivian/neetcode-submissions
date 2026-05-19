class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        list_of_dic_words = []
        for word in strs:
            current_word_dict = {}
            for letter in word:
                current_word_dict[letter] = word.count(letter)
            list_of_dic_words.append(current_word_dict)

        final_list = []
        visited = set()  

        for i, dicto in enumerate(list_of_dic_words):
            if i in visited: 
                continue
            
            current_group = [strs[i]]
            visited.add(i)

            for j, comp_dicto in enumerate(list_of_dic_words):
                if j not in visited and dicto == comp_dicto:
                    current_group.append(strs[j])
                    visited.add(j)

            final_list.append(current_group)

        return final_list