#!/usr/bin/python
# -*- coding: utf-8 -*-
# editor: mufei(ypdh@qq.com tel:+086 15712150708)
'''
Mufei _ __ ___   ___   ___  / _| ___(_)
| '_ ` _ \ / _ \ / _ \| |_ / _ \ |
| | | | | | (_) | (_) |  _|  __/ |
|_| |_| |_|\___/ \___/|_|  \___|_|
'''

#openocr
#tesseract-ocr
#PaddleOCR
#cnocr cnstd 
#chineseocr


import os, time, warnings

try:
    from cnocr import CnOcr 
except ImportError:
    warnings.warn('Please Import cnocr TO pip')
    CnOcr = None
    
from moofei._find import _py, _strtypes,_find_func,_search_func

try:
    from .cplugin_fix import _StringIO, StringIO, cPlugin_Fix
except (ImportError,ValueError):
    from cplugin_fix import _StringIO, StringIO, cPlugin_Fix
    

class cPlugin_Fix_Image(cPlugin_Fix):
    def is_enable(self):
        return CnOcr

    def image2pic(self, fix):
        '''
        picpath = cPlugin_Fix_Image(picpath, fp=pic).image2png()
        '''
        assert fix[0]=='.'
        if self.fpath.endswith(fix) and os.path.isfile(self.fpath) and not self.fp:
            return self.fpath
        else:
            from PIL import Image, ImageFile
            ImageFile.LOAD_TRUNCATED_IMAGES = True
            path = self.fpath.rsplit('.', 1)[0]+fix
            im = Image.open(self.fp or self.fpath)
            im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE,colors=256)
            try:
                im.save(path, optimize=True)
            except:
                print('save image2pic error')
                im.save(path)
        return path

    def image2png(self):
        return self.image2pic('.png')
                
    def all_texts(self):
        '''
        CnOCR 从 V2.2 开始，内部自动调用文字检测引擎 CnSTD 进行文字检测和定位。
        所以 CnOCR V2.2 不仅能识别排版简单的印刷体文字图片，如截图图片，扫描件等，
        也能识别一般图片中的场景文字。
        '''
        #低版本~~ CnOcr (name=fpath).ocr(fpath): [['大', '背', '景'], ['电', '子', '卷', '宗']]
        #低版本   CnOcr2(name=fpath).ocr(fpath): [(['大', '背', '景'], array([0.9999987, 1. , 1.], dtype=float32)),...]
        #高版本   [{'text': '*案号', 'score': 0.92, 'position': array([[223., 167.],], dtype=float32)}, ...]
        Ls = []
        fpath = self.get_tempfile_or_path(suffix=True)
        #print(fpath)
        cn_ocr = CnOcr(name=fpath)
        ocr_res = cn_ocr.ocr(fpath)
        for e in ocr_res:
            if not e: continue
            if isinstance(e, dict):
               s = e['text'] + ' '
            else:
                s = ''.join(e)
            Ls.append(s)     
        text = ''.join(Ls)
        return text
        
    def __all_texts_xxx(self):
        Ls = []
        try:
            from cnstd import CnStd
        except:
            warnings.warn('Please Import cnstd TO pip')
            CnStd = None
        try:
            import mxnet 
        except:
            warnings.warn('Please Import mxnet TO pip')
            mxnet = None
        
        t0 = time.time()
        fpath = self.get_tempfile_or_path()
        #cn_ocr = CnOcr(name=fpath); is_2 = False
        cn_ocr = self.get_ocr()(name=fpath); is_2 = True
        t1 = time.time()
        
        if CnStd:
            #rotated_bbox: 是否支持旋转检测带角度 默认为True, 为了减少模型计算量,水平文字可以设rotated_bbox为False
            std = CnStd(rotated_bbox=True)
            box_info_list = std.detect(fpath)
            print(t1-t0, 'CnStd::std.detect(fpath)')
        elif  mxnet and 0:
            img = mxnet.image.imread(fpath, 1).asnumpy()
            line_imgs = line_split(img, blank=True)
            box_info_list = [line_img for line_img, _ in line_imgs]
        else:
            box_info_list = []
            #ocr_res = cn_ocr.ocr_for_single_line(fpath)
            ocr_res = cn_ocr.ocr(fpath)
            #if is_2: ocr_res = ocr_res[0]
            print(ocr_res)
            for e in ocr_res: 
                s = ''.join(e[0])
                Ls.append(s)
            #print('ocr result: %s' % ''.join(ocr_res), len(box_info_list))
            #s = ''.join(ocr_res)
            #Ls.append(s)
        if isinstance(box_info_list, dict):
            box_info_list = box_info_list['detected_texts']
            rotated_angle = box_info_list['rotated_angle']
            
        for box_info in box_info_list:
            cropped_img = box_info['cropped_img']  # 检测出的文本框
            #(['王', '∶'], array([0.99952316, 0.83975214], dtype=float32))
            ocr_res = cn_ocr.ocr_for_single_line(cropped_img) #ocr_for_single_lines
            #print('ocr result: ', ocr_res, len(box_info_list))
            if is_2: ocr_res = ocr_res[0]
            print('ocr result: %s' % ''.join(ocr_res), len(box_info_list))
            s = ''.join(ocr_res)
            Ls.append(s)
        
        print(time.time()-t1, 'CnOcr(fpath)')
        text = '\n'.join(Ls)
        return text
    
    @classmethod    
    def get_ocr(cls):
        '识别字符结果的概率值'
        #(['大', '背', '景'], array([0.9999987, 1. , 1.], dtype=float32))
        try:
            from cnocr.cn_ocr import CnOcr,np,CtcMetrics
        except:
            #新版本自带 score
            from cnocr.cn_ocr import CnOcr
            return CnOcr
        class CnOcr2(CnOcr):
            def _del_repeat(self, a):
                # a = [1, 0, 0, 2, 2, 2]
                opt = [1] * len(a)
                for i in range(len(a)):
                    if a[i] == 0:
                        opt[i] = 0
                        continue
                    if i >= 1:
                        if a[i] == a[i - 1]:
                            opt[i] = 0
                return np.nonzero(np.array(opt))

            def _gen_line_pred_chars(self, line_prob, img_width, max_img_width):
                """
                Get the predicted characters.
                :param line_prob: with shape of [seq_length, num_classes]
                :param img_width:
                :param max_img_width:
                :return:
                """
                class_ids = np.argmax(line_prob, axis=-1)
                indexs = self._del_repeat(class_ids)
                probs = np.max(line_prob, axis=-1)
                fin_probs = probs[indexs]
                # print('==fin_probs:', fin_probs)
                # print('==len(fin_probs):', len(fin_probs))
                if img_width < max_img_width:
                    comp_ratio = self._hp.seq_len_cmpr_ratio
                    end_idx = img_width // comp_ratio
                    if end_idx < len(class_ids):
                        class_ids[end_idx:] = 0
                prediction, start_end_idx = CtcMetrics.ctc_label(class_ids.tolist())
                # print('==prediction:', prediction)
                alphabet = self._alphabet
                res = [alphabet[p] if alphabet[p] != '<space>' else ' ' for p in prediction]
                return (res, fin_probs)
        return CnOcr2
        
        
     
