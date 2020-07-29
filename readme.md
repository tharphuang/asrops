#asrops说明

## 整体架构
  1. 前后端分离，后端框架为django框架、前端框架为vue。  
  2. 对应程序包结构：  
  app为python3下django框架model和controller层主体结构，app主要以接口的方式，为前端提供处理能力。
  appVue为vue框架下程序前端view层主体结构。
  
## 运行方式  
  1. asrops目录下：  
  `python3 manage.py runserver 0:8080`
  2. appVue目录下：
  `npm run dev`
  
  