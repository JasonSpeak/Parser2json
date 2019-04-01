## Parser2json  
**Parser2json** is a file parser to convert configure file to json file  
Such as **.xml, .dat, .ini, .config, .yaml**   



There are four functions in this file

- `dat2json(datFile_location,keyList,splitStr)` convert .dat files to .json files
- `xml_config2json(xml_configFile_Location)` convert .xml or .config files to .json files
- `ini2json(iniFile_Location)`convert .ini files to .json files
- `yaml2json(yamlFile_Location)`convert .yaml files to .json files

**module [yaml](https://github.com/yaml/pyyaml) is needed**  
`pip install pyyaml`


*The **xml_config2json** function used [xmltodist](https://github.com/martinblech/xmltodict) from gayhub*  

**Example:**  

>`import parser2json`  
`'''test for dat2json'''`  
`keyList = ["1","2","3"]`  
`parser2json.dat2json("test_dat2json.dat",keyList,",")`  

