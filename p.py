import re

r2=r'\d+'
with open('1.txt','r')as f:
    x=f.readline()
    #print(x)
    x = f.readline()
    data={'东街口/三坊七巷':0,
          '五一广场/古田路':0,

          }
    while len(x)>0:

        y=str(x)
        #print(x)
        p=re.compile(',([^,]+?)\n')
        p1=re.compile('\d+')
        #print(x)
        d=p.findall(y)
        d1= p1.findall(y)
        m=str(d[0])
        n=int(d1[len(d1)-1])
      #  print(d[0],d1[len(d1)-1])
        try :
            data[m]+=n
        except KeyError:
            data.update({m:n})
        x = f.readline()
    for k in sorted(data, key=data.__getitem__, reverse=True):
        print(k, data[k])
