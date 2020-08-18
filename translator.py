import pandas as pd
import re
class Translator:
    def __init__(self, file_loc, new_lang):
        '''
        :param file_loc: The original file that has to check
        :param new_lang: To which language the file has to be converted
        '''
        self.xmlfile = file_loc
        self.new_lang = new_lang
        self.df = pd.read_excel("JP_lookup.xlsx")

    def lookup_fun(self, inp):
        '''
        This function look-up into the xls to ensure any word reference presence or not.
        :param inp: Each line(tag) of the original xml sheet
        :return: returns the equivalent foreign language word if reference available
        '''
        for index, row in self.df.iterrows():
            if row['English'] in inp:
                if self.new_lang == 'jp':
                    return row['Japanese']
                elif self.new_lang == 'ge':
                    return row['German']
                elif self.new_lang == 'fr':
                    return row['French']
        return None

    def data_parse(self):
        '''
        The method opens the original xml file and iterate through all the lines and modify the content with the
        equivalent foreign language
        :return: the translated content
        '''
        with open(self.xmlfile, "r") as xmldata:
            translated_data = []
            for line in xmldata.readlines():
                is_present = self.lookup_fun(line)
                if is_present:
                    updated = re.sub('(<.*?>)(.*)(</.*?>)',r"\1"+is_present+r"\3",line)
                    translated_data.append(updated)
                else:
                    translated_data.append(line)
        return translated_data

    def prapare_newxml(self):
        '''
        The method will create a new(translated) file: ex: xml1_jp.xml
        '''
        new_data = self.data_parse()
        with open(self.xmlfile+'_'+self.new_lang, "w", encoding="utf-8") as f:
            f.writelines(new_data)
        print("Translation completed")

jp = Translator('xml2.xml','jp') #['jp': 'Japanese', 'ge': 'German', 'fr': 'French']
jp.prapare_newxml()