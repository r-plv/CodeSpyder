#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


# In[2]:


def add_data(d1):
    d2={}
    n = int(input('Enter no of records you want to enter :'))
    for i in range(n):
        k = int(input('Enter choice of data type you want to insert : \n 1.Stud_Id \n 2.Name \n 3.Branch \n 4.Mobile_No \n 5.Email_Id \n'))
        if k==1:
            key='stud_id'
            d2.update({key:input('Enter stud_id :')})
        elif k==2:
            key ='name'
            d2.update({key:input('Enter name :')})
        elif k==3:
            key='branch'
            d2.update({key:input('Enter branch :')})
        elif k==4:
            key='mobile_no'
            d2.update({key:int(input('Enter mobile no :'))})
        elif k==5:
            key='email_id'
            d2.update({key:input('Enter email id :')})
    clear_output()
    record_key = len(d1)+1
    d1.update({record_key:d2})
    print('Record updated..\n')
    return d1


# In[3]:


def remove_data(d1):
    print('Records available : ',d1)
    n = int(input('How many record you want to remove :'))
    for i in range(n):
        r = int(input('Enter which record you want to delete : '))
        d1.pop(r)
    clear_output()
    print(n,'-Record removed..\nUpdated record')
    return d1


# In[4]:


def find_record(d1):
    n = int(input('Enter record no .. You want to find ..'))
    record = d1.get(n)
    clear_output()
    return record


# In[5]:


def sort_data(d1):
    column = input('Enter column name : \n stud_id \n name \n branch \n mobile_no \n email_id')
    sorted_data = sorted(d1.items(), key = lambda x: x[1][column])
    clear_output()
    print('Data after Ascending sort..')
    return sorted_data


# In[ ]:




