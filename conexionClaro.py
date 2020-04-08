from datetime import datetime
import json
import xml
import requests
import configparser
import random
import re
import sys
from random import randint



class Claroxml:
    url = "http://172.22.87.181:9898/pretups/C2SReceiver?REQUEST_GATEWAY_CODE=9003275863&" \
              "REQUEST_GATEWAY_TYPE=EXTGW&LOGIN=SP9003275863_EXTGW&PASSWORD=89b87741ca3f73b0b282ae165bad7501&" \
              "SOURCE_TYPE=XML&SERVICE_PORT=190"


    pre_tup = """<?xml version="1.0"?><!DOCTYPE COMMAND PUBLIC "-//Ocam//DTD XML Command 1.0//EN" "xml/command.dtd"><COMMAND><TYPE>EXRCTRFREQ</TYPE><DATE>{fec_hor}</DATE><EXTNWCODE>CC</EXTNWCODE><MSISDN>3126658472</MSISDN><PIN>2614</PIN><LOGINID></LOGINID><PASSWORD></PASSWORD><EXTCODE>9003275863</EXTCODE><EXTREFNUM>{extrefnum}</EXTREFNUM><MSISDN2>{num}</MSISDN2><AMOUNT>{mon}</AMOUNT><LANGUAGE1>0</LANGUAGE1><LANGUAGE2>0</LANGUAGE2><SELECTOR>1</SELECTOR><INFO1>COD00113</INFO1><INFO2></INFO2><INFO3></INFO3><INFO4></INFO4></COMMAND>"""
    vas_pdd = """<?xml version="1.0"?><!DOCTYPE COMMAND PUBLIC "-//Ocam//DTD XML Command 1.0//EN" "xml/command.dtd"><COMMAND><TYPE>VASEXTRFREQ</TYPE><DATE>{fec_hor}</DATE><EXTNWCODE>CC</EXTNWCODE><MSISDN>3126658472</MSISDN><PIN>2614</PIN><LOGINID></LOGINID><PASSWORD></PASSWORD><EXTCODE>9003275863</EXTCODE><EXTREFNUM>{extrefnum}</EXTREFNUM><MSISDN2>{num}</MSISDN2><AMOUNT>{mon}</AMOUNT><LANGUAGE1>0</LANGUAGE1><LANGUAGE2>0</LANGUAGE2><SELECTOR>{sel}</SELECTOR><INFO1>COD00113</INFO1><INFO2></INFO2><INFO3></INFO3><INFO4></INFO4></COMMAND>"""
    vas_dth_tv = """<?xml version="1.0"?><!DOCTYPE COMMAND PUBLIC "-//Ocam//DTD XML Command 1.0//EN" "xml/command.dtd"><COMMAND><TYPE>EXDTHTRFREQ</TYPE><DATE>{fec_hor}</DATE><EXTNWCODE>CC</EXTNWCODE><MSISDN>3126658472</MSISDN><PIN>2614</PIN><EXTCODE>9003275863</EXTCODE><EXTREFNUM>{tra_ids}</EXTREFNUM><MSISDN2>{num}</MSISDN2><AMOUNT>{mon}</AMOUNT><LANGUAGE1>0</LANGUAGE1><LANGUAGE2>0</LANGUAGE2><SELECTOR>{sel}</SELECTOR><INFO1>COD00113</INFO1></COMMAND>"""
    status_tra=  """<?xml version="1.0"?><!DOCTYPE COMMAND PUBLIC "-//Ocam//DTD XML Command 1.0//EN""xml/command.dtd"><COMMAND><TYPE>EXRCTRFREQ</TYPE><DATE>{fec_hor}</DATE><EXTNWCODE>CC</EXTNWCODE><MSISDN>3126658472</MSISDN><PIN>2614</PIN><LOGINID></LOGINID><PASSWORD></PASSWORD><EXTCODE>9003275863</EXTCODE><EXTREFNUM>{extrefnum}</EXTREFNUM><TXNID></TXNID><LANGUAGE1>0</LANGUAGE1></COMMAND>"""

    paq = {'100': ['50000', 6000, 'Navega 120MB + 30 MIN + 1.000 mensajes', 'xml_paq_tod'],
           '101': ['50001', 10000, 'Navega 200MB + 70 MIN + 1.000 mensajes', 'xml_paq_tod'],
           '102': ['50002', 20000, 'Navega 500MB + 150 MIN + 1.000 mensajes', 'xml_paq_tod'],
           '103': ['50003', 40000, 'Ilimitados 30 Dias', 'xml_paq_tod'],
           '112': ['50010', 3000, 'Navega 60MB + 50 MIN + 500 mensajes', 'xml_paq_tod'],
           '104': ['50030', 2000, 'NAVEGA_100MB', 'xml_paq_tod'],
           '105': ['50031', 4000, 'NAVEGA_220MB', 'xml_paq_tod'],
           '118': ['50014', 5000, 'PAQUETE_100_MIN_TAT', 'xml_paq_tod'],
           '119': ['50015', 9900, 'PAQUETE_200_MIN_TAT', 'xml_paq_tod'],
           '120': ['31272', 2500, 'Paquete de Snapchat 1 Dia TAT', 'xml_paq_tod'],
           '121': ['31260', 3000, 'Paquete de Youtube por 1 hora TAT', 'xml_paq_tod'],
           '128': ['31278', 2500, 'Paquete de Instagram por 1 dia TAT', 'xml_paq_tod'],
           '129': ['31266', 1000, 'Paquete de Waze por 1 dia TAT', 'xml_paq_tod'],
           '130': ['50047', 10000, 'Paquete_Todo_incluido_ilimitados_1GB_7DIAS', 'xml_paq_tod'],
           '131': ['50048', 20000, 'Ilimitados 15DIAS', 'xml_paq_tod'],
           '132': ['500062', 21900, 'INTERNET_INALAMBRICO_2GB', 'xml_paq_tod'],
           '133': ['500014', 39900, 'INTERNET_INALAMBRICO_4GB', 'xml_paq_tod'],
           '134': ['500015', 59900, 'INTERNET_INALAMBRICO_10GB', 'xml_paq_tod'],
           '135': ['500016', 99900, 'INTERNET_INALAMBRICO_20GB', 'xml_paq_tod'],
           '136': ['50049', 2000, 'PAQUETE_LARGA_DISTANCIA_VENEZUELA_2000', 'xml_paq_tod'],
           '137': ['50050', 5000, 'PAQUETE_LARGA_DISTANCIA_VENEZUELA_5000', 'xml_paq_tod'],
           '122': ['50027', 6000, 'Ilimitados 6 Días', 'xml_paq_tod'],
           '123': ['50028', 10000, 'Ilimitados 10 Días', 'xml_paq_tod'],
           '124': ['50029', 20000, 'Ilimitados 20 Dias', 'xml_paq_tod'],
           '125': ['50023', 10000, 'Navega 1000MB', 'xml_paq_tod'],
           '126': ['50024', 20000, 'Navega 2000MB', 'xml_paq_tod'],
           '127': ['50064', 30000, 'PAQUETE_REVENTA', 'xml_paq_tod'],
           '107': ['50007', 2000, 'Navega 40MB', 'xml_paq_tod'],
           '108': ['50008', 4000, 'Navega 120MB', 'xml_paq_tod'],
           '109': ['50009', 15000, 'Navega 500MB', 'xml_paq_tod'],
           '110': ['50019', 9000, 'Chat de WhatsApp 15 dias', 'xml_paq_tod'],
           '106': ['50020', 18000, 'Chat de WhatsApp 30 dias', 'xml_paq_tod'],
           '111': ['50012', 3000, 'Paquete 60 MIN TAT 2 DIAS', 'xml_paq_tod'],
           '117': ['50017', 1000, 'Paquete 20 MIN TAT POR 24H', 'xml_paq_tod'],
           '113': ['830', 32000, 'Tv prepago 15 dias estandar uno deco', 'xml_paq_dth'],
           '114': ['831', 37000, 'Tv prepago 15 dias estandar dos deco', 'xml_paq_dth'],
           '115': ['832', 55000, 'Tv prepago 30 dias estandar un deco', 'xml_paq_dth'],
           '116': ['833', 64000, 'Tv prepago 30 dias estandar dos deco', 'xml_paq_dth'],
           '138': ['50063', 15000, 'PAQUETE_REVENTA_15000', 'xml_paq_tod'],
           '139': ['11099', 2000, 'PAQUETE_LDI_USA_MEX_10MIN_30D', 'xml_paq_tod'],
           '140': ['11100', 5000, 'PAQUETE_LDI_USA_MEX_30MIN_30D', 'xml_paq_tod'],
           '141': ['31492', 15000, 'PAQUETE_INSTAGRAM_7D', 'xml_paq_tod'],
           '142': ['31493', 15000, 'PAQUETE_SNAPSHAT_7D', 'xml_paq_tod'],
           '143': ['31494', 3000, 'PAQUETE_WAZE_7D', 'xml_paq_tod'],
           '144': ['50065', 5000, 'NAVEGA_ILIMITADO_2HORAS', 'xml_paq_tod'],
           '145': ['111123', 10000, 'PAQUETE_LDI_VENEZUELA_10000', 'xml_paq_tod'],
           '3': ['3', 0, 'RECARGA', 'rec'],
           's': ['', 0, 'CONSULTA', 'status']}

    def ramid(self):
        return ''.join(random.choice('0123456789ABCDEFabcdefHIJKhijkOo') for _ in range(20))

    def cab_pru(self):

        headers = {
            'POST URL HTTPs': '',
            'Content-Type': 'xml',
            'Connection': 'close',
            'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        }
        return headers

    def cab(self):

        headers = {
            'POST URL HTTPs': '',
            'Content-Type': 'xml',
            'Connection': 'close',
        }
        return headers

    def rec(self, num=3154251382, mon=1000, cod_dig='3'):
        print('[{} - {} - {} - {}] ENTRADA'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), num, mon, cod_dig),
              flush=True)
        pro = self.paq[cod_dig]
        mon = int(mon)
        fec_hor = datetime.now().strftime('%d/%m/%y')
        tra_ids = self.ramid()
        extrefnum = "75863{}{}".format(datetime.now().strftime('%Y%m%d%H%M'), randint(000, 999))
        try:
            if pro[3] == 'rec':
                if 1000 >= mon >= 100000:
                    return json.dumps({'respuesta': 'MONTO INVALIDO'})
                dat = {'num': num, 'mon': mon, 'fec_hor': fec_hor, 'tra_ids': tra_ids, 'extrefnum': extrefnum}
                data = self.pre_tup.format(**dat)
            elif pro[3] == 'xml_paq_dth':
                dat = {'num': num, 'mon': pro[1], 'fec_hor': fec_hor, 'tra_ids': tra_ids, 'sel': pro[0]}
                data = self.vas_dth_tv.format(**dat)
            elif pro[3] == 'xml_paq_tod':
                dat = {'num': num, 'mon': pro[1], 'fec_hor': fec_hor, 'tra_ids': tra_ids, 'sel': pro[0],
                       'extrefnum': extrefnum}
                data = self.vas_pdd.format(**dat)
            else:
                return json.dumps({'respuesta': 'TIPO NO CONFIGURADO'})

            print('[{} - {} - {} - {}] ENVIO [{}]'.format(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'), num, mon, cod_dig, data), flush=True)
            try:

                req = requests.post(self.url, data=data, headers=self.cab(), timeout=40, verify=False)

                print('[{} - {} - {} - {}] REQ [{}]'.format(
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'), num, mon, cod_dig, req), flush=True)
                if req.status_code == 200:
                    print('[{} - {} - {} - {}] RESPUESTA [{}]'.format(
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'), num, mon, cod_dig, req.text), flush=True)
                    res_pon = xmltodict.parse(req.text)
                    cod_sta = res_pon['COMMAND']['TXNSTATUS']
                    txt_msg = res_pon['COMMAND']['MESSAGE']
                    tx_nid = '0'
                    if 'TXNID' in res_pon['COMMAND']:
                        tx_nid = res_pon['COMMAND']['TXNID']
                    if cod_sta == '200': # and 'Transaccion Exitosa' in txt_msg:
                        return json.dumps({"respuesta": "Recarga exitosa", "txnid": tx_nid})
                    else:
                        return json.dumps({"respuesta": "[{}] {}".format(cod_sta, txt_msg), "txnid": tx_nid})
                else:
                        resp_con = self.con(extrefnum)
                        if 'Transaccion Exitosa' in resp_con:
                            return json.dumps({"respuesta": "Recarga exitosa", "txnid": tx_nid})
                        else:
                           return json.dumps({"respuesta": "[{}] Sin respuesta".format(req.status_code)})
            except requests.ConnectionError as err:
                print("NO RESPONDEEE")
                resp_con = self.con(extrefnum)
                print(resp_con)
                if 'Transaccion Exitosa' in resp_con:
                    return json.dumps({"respuesta": "Recarga exitosa", "txnid": tx_nid})
                else:
                    print('[{} - {} - {} - {}] ERROR [{}]'.format(
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'), num, mon, cod_dig, err), flush=True)
                    res = 'EN MANTENIMIENTO'
                    print(res)
                    return res
        except ConnectionError as err:
            print("AQUIIII VOY")

            resp_con = self.con(extrefnum)
            if 'Transaccion Exitosa' in resp_con:
                return json.dumps({"respuesta": "Recarga exitosa", "txnid": tx_nid})
            else:
                print('[{} - {} - {} - {}] ERROR [{}]'.format(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'), num, mon, cod_dig, err), flush=True)
                res = 'EN MANTENIMIENTO'
                return res
            
    def con(self, extrafum):
        fec_hor = datetime.now().strftime('%d/%m/%y')
        tra_ids = self.ramid()
        dat = {'extrefnum': extrafum,'fec_hor': fec_hor,'tra_ids': tra_ids}
        data = self.status_tra.format(**dat)
        try:
            req = requests.post(self.url, data=data, headers=self.cab(), timeout=60, verify=False)
            if req.status_code == 200:
                print('[{} - {}] CONSULTA [{}]'.format(
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'), tra_ids_vie, req.text), flush=True)
                res_pon = xmltodict.parse(req.text)
                cod_sta = res_pon['COMMAND']['TXNSTATUS']
                txt_msg = res_pon['COMMAND']['MESSAGE']
                tx_nid = '0'
                if 'TXNID' in res_pon['COMMAND']:
                    tx_nid = res_pon['COMMAND']['TXNID']
                if cod_sta == '200':
                    return json.dumps({"respuesta": "Recarga exitosa {}".format(txt_msg), "txnid": tx_nid})
                else:
                    return json.dumps({"respuesta": "[{}] {}".format(cod_sta, txt_msg), "txnid": tx_nid})
            else:
                return json.dumps({"respuesta": "[{}] Sin respuesta".format(req.status_code)})
        except requests.ConnectionError:
            print('[{} - {} - {}] AUTO_CON_ERROR [{}]')#.format(
                #datetime.now().strftime('%Y-%m-%d %H:%M:%S'), tra_ids_vie, con, err), flush=True)
            return json.dumps({"respuesta": "[ERR] Sin respuesta"})
            

    
           
if __name__ == '__main__':
  Claroxml().rec(num=3154251382, mon=1000, cod_dig='3')
    