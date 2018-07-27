# Gain cbooo_film message
using movies.txt get movie_ids to log on movie sites, then gain basic message about the movie
## Main codes
* movies.txt <br>
get ids to complete url <br>
* cbooo_message.py <br>
crawl data from url <br>
* read.py <br>
gain movies imformation from json file <br>
* try.py <br>
get the picture about the movie in movie.txt
## main function
***cbooo_messge.py*** 
* get_name()　　　　　　　　//獲取電影名字     <br>
* get_film()　　　　　　　　//獲取電影類型     <br>
* get_length()　　　　　　　//獲取電影片長     <br>
* get_data()　　　　　　　　//獲取電影上映時間  <br>
* get_country()　　　　　　//獲取電影國家及地區<br>
* get_director()　　　　　　//獲取電影導演     <br>
* get_actor()　　　　　　　//獲取電影演員     <br>
* get_company()　　　　　　//獲取電影制作工資  <br>
* get_distirbutor()　　　　//獲取電影發行公司  <br>
* get_total()　　　　　　　　//獲取電影累計票房  <br>
***try.py***
* get_name()　　　　　　　　　//獲取電影名字 <br>
* get_cover()　　　　　　　　//獲取電影海報 <br>
## Operating environment
Based on python3 and selenium, first need to install:
* requests
* phantomjs
* re
* urllib
* json
## Operation instructions
|cbooo_message.py|　　read.py |
|:---|:---|
|**first step** <br> used to get <br> all films message <br> from url|**second step** <br> used to get <br> one film <br> more detail message|
## Sample
Take [Once Upon a Time(三生三世十里桃花)](http://www.cbooo.cn/m/629924) as an example <br>
1.use xpath and selenium to get all message about the film. <br>
![sample1](https://github.com/GuaTing/chinese-movie/blob/master/sample1.jpeg) <br>
2.save the message as json_file <br>
![sample2](https://github.com/GuaTing/chinese-movie/blob/master/sample2.png) <br>
## designation
|name|id|film|data|country|distributor|company|director|actor|total|length|
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|film name|film id|film type|film <br> release date|film company|film <br> ｄistribution companies|film <br> ｐroduction company|film director|film <br> main actor|film total <br> box office|film ｌｅｎｇｔｈ| <br>
３．get detil messge
