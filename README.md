# Phoenix


*CV library for image data augmentation*

![Phoenix](https://github.com/Airspace-02/phoenix/workflows/Sphinx/badge.svg?branch=master)

,-.----.                                                                          
\    /  \     ,---,                                                               
|   :    \  ,--.' |                                          ,--,                 
|   |  .\ : |  |  :        ,---.                    ,---,  ,--.'|                 
.   :  |: | :  :  :       '   ,'\               ,-+-. /  | |  |,      ,--,  ,--,  
|   |   \ : :  |  |,--.  /   /   |    ,---.    ,--.'|'   | `--'_      |'. \/ .`|  
|   : .   / |  :  '   | .   ; ,. :   /     \  |   |  ,"' | ,' ,'|     '  \/  / ;  
;   | |`-'  |  |   /' : '   | |: :  /    /  | |   | /  | | '  | |      \  \.' /   
|   | ;     '  :  | | | '   | .; : .    ' / | |   | |  | | |  | :       \  ;  ;   
:   ' |     |  |  ' | : |   :    | '   ;   /| |   | |  |/  '  : |__    / \  \  \  
:   : :     |  :  :_:,'  \   \  /  '   |  / | |   | |--'   |  | '.'| ./__;   ;  \ 
|   | :     |  | ,'       `----'   |   :    | |   |/       ;  :    ; |   :/\  \ ; 
`---'.|     `--''                   \   \  /  '---'        |  ,   /  `---'  `--`  
  `---`                              `----'                 ---`-'                
                                                                                  

Phoenix is a CV library for massively scalable image data augmentation specifically built
for automotive deep learning usecases.

## Installing locally

With your `venv` activated:

```bash
$ python setup.py install
```

### Running tests

From your activated `.venv` run:

```bash
$ make test
```

## usage

Sample Configuration json for Phoenix

```
{
            "input_dir" : "images",
            "output_dir" : "output",
            "annotation_dir" : "annotations",
            "annotation_format" : "pascal_voc",
            "mask_dir" : "mask"
            "sample" : 5000,
            "multi_threaded" : true,
            "run_all" : false,
            "batch_ingestion": true,
            "internal_batch": 20,
            "save_annotation_mask" : false,
            "operations":[
                {
                    "operation": "DarkenScene",
                    "operation_module" : "sphinx.augmentation",
                    "args": {
                        "probability": 0.7,
                        "darkness" : 0.5,
                        "is_mask" : true,
                        "mask_label" : 2,
                        "is_annotation" : true,
                        "annotation_label : 1
                    }
                },
                {
                    "operation": "Equalize",
                    "operation_module" : "sphinx.augmentation",
                    "args": {
                        "probability": 0.5,
                        "is_mask" : true,
                        "label" : 2
                    }
                },
                {
                    "operation": "RadialLensDistortion",
                    "operation_module" : "sphinx.augmentation",
                    "args": {
                        "probability": 0.5,
                        "is_annotation" : true,
                        "distortiontype" : "NegativeBarrel",
                        "is_mask" : true,
                    }
                }
            ]
        }
```

```
from phoenix.augmentation import Builder
pipeline = Builder(config_json="config.json")
pipeline.process_and_save()
```

