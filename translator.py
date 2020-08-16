import pandas as pd
import re
class Translator:
    def __init__(self, file_loc, new_lang):
        self.xmlfile = file_loc
        self.new_lang = new_lang
        self.df = pd.read_excel("JP_lookup.xlsx")
    def lookup_fun(self, inp):
        for index, row in self.df.iterrows():
            if row['English'] in inp:
                if self.new_lang == 'jp':
                    return row['Japanese']
        return None

    def data_parse(self):
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
        new_data = self.data_parse()
        with open(self.xmlfile+'_'+self.new_lang, "w", encoding="utf-8") as f:
            f.writelines(new_data)
        print("success")



jp = Translator('xml2.xml','jp')
jp.prapare_newxml()