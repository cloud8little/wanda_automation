from behave import *
from configuration.globalUtil import GlobalSetting
from lib.db_lib import MysqlLib
import os
import time,datetime,sys
import codecs

default_config = GlobalSetting.get_value('')
env = 'SIT'
env_config = default_config[env]
mysql_config = env_config['MYSQL']
mysql_conn = MysqlLib(mysql_config['host'], mysql_config['username'], mysql_config['password'])

@given('I select recordnumber from {table}')
def step_impl(context,table):
    sql_sentence = "select count(*) from loancore.user_personal_basic_info; "
    print(sql_sentence)
    context.mysql_result = mysql_conn.execute_sql(sql_sentence, 'loancore')
    for row in context.mysql_result:
        print(row)
    pass

@then('I query refused list')
def step_impl(context):
    review_type = ['0','1','2']
    status = '4'
    approve_result = '1'
    tenant_id = '000'
    limit = [0,20]
    sql_sentence = 'select id, tenant_id, serial_id, apply_id, flow_id, icdm_id, user_id, apply_amount, level, sort, user_name, user_mobile, id_kind, id_no, product_id, product_name, apply_period, apply_unit, apply_time, channel_no, org_id, marketing_id, cooprate_org_id, status,current_node_code, current_node_name, current_node_taskid, current_operator_id, rulecode, holdon_flag, holdon_time, holdon_reason, process_id, review_type, biz_type, create_time,      update_time, receive_time, manage_id, manage_name, approve_result, refuse_code, refuse_reason, finish_flag, finish_time, auto_pass_flag, exception_flag, history_exception, exception_code, man_approve_amount, dt_approve_amount, dt_approve_result, dt_refuse_code, current_roleId from loanpublic.flow_biz_apply f  WHERE (  review_type in  ( %s,%s,%s) and status <> %s and approve_result = %s and tenant_id = %s ) limit %s,%s;'
    context.mysql_result = mysql_conn.execute_sql(sql_sentence, 'loanpublic',(review_type[0],review_type[1],review_type[2],status,approve_result,tenant_id,limit[0],limit[1]))
    pass

@then('I save the sql result as')
def step_impl(context):
    timestr = ''
    if 'timestamp' in context.table.headings:
        if context.table['timestamp']:
            timestr = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    for row in context.table:
        print(row)
        filename = row['filename']
        currentfilepath = os.path.join(os.path.dirname(__file__))
        print(filename)
        print(currentfilepath)
        print(timestr)
        testfilepath = (os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../testdata/database/%s%s.%s' % (row['filename'],timestr,row['type']))))
        print(testfilepath)
        with codecs.open(testfilepath,'w','utf-8') as savedata:
            for r in context.mysql_result:
                print(r)
                print(type(r))
                for key in r.keys():
                    print(type(r[key]))
                    if 'datetime.datetime' in str(type(r[key])):
                        savedata.write(r[key].strftime('%Y-%m-%d %H:%M:%S'))
                    elif  'int' in str(type(r[key])):
                        savedata.write(str(r[key]))
                    elif 'NoneType' in str(type(r[key])):
                        savedata.write('Null')
                    elif 'decimal.Decimal' in str(type(r[key])):
                        savedata.write(str(r[key]))
                    else:
                        savedata.write(r[key].encode('utf-8', 'ignore').decode('utf-8'))
                    savedata.write(",")
                savedata.write("\n")
    pass