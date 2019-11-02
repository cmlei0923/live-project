import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class RestaurantRank{
    public static shop shop1=new shop();
    public static shop shop2=new shop();
    public static shop shop3=new shop();
    public static shop shop4=new shop();
    public static List<shop> shopList=new ArrayList<>();
    public static class shop {
        String[] info = new String[10000];
        String[] name=new String[10000];
        String[] address=new String[10000];
        float[] score = new float[10000];
        int[] price = new int[10000];
        int x;
        int type;
        private void Shop() {
            x = 0;
        }
    }

    public static void sort(int x){
        if(x==1){
            for(int i=0;i<shop1.x-1;i++){
                for(int j=i+1;j<shop1.x;j++){
                    if(shop1.score[i]<shop1.score[j]){
                        float tmp1=shop1.score[i];
                        shop1.score[i]=shop1.score[j];
                        shop1.score[j]=tmp1;
                        String s=shop1.info[i];
                        shop1.info[i]=shop1.info[j];
                        shop1.info[j]=s;
                        int tmp2=shop1.price[i];
                        shop1.price[i]=shop1.price[j];
                        shop1.price[j]=tmp2;
                    }
                }
            }
        }
        else if(x==2){
            for(int i=0;i<shop2.x-1;i++){
                for(int j=i+1;j<shop2.x;j++){
                    if(shop2.score[i]<shop2.score[j]){
                        float tmp1=shop2.score[i];
                        shop2.score[i]=shop2.score[j];
                        shop2.score[j]=tmp1;
                        String s=shop2.info[i];
                        shop2.info[i]=shop2.info[j];
                        shop2.info[j]=s;
                        int tmp2=shop2.price[i];
                        shop2.price[i]=shop2.price[j];
                        shop2.price[j]=tmp2;
                    }
                }
            }
        }
        else if(x==3){
            for(int i=0;i<shop3.x-1;i++){
                for(int j=i+1;j<shop3.x;j++){
                    if(shop3.score[i]<shop3.score[j]){
                        float tmp1=shop3.score[i];
                        shop3.score[i]=shop3.score[j];
                        shop3.score[j]=tmp1;
                        String s=shop3.info[i];
                        shop3.info[i]=shop3.info[j];
                        shop3.info[j]=s;
                        int tmp2=shop3.price[i];
                        shop3.price[i]=shop3.price[j];
                        shop3.price[j]=tmp2;
                    }
                }
            }
        }
        else if(x==4){
            for(int i=0;i<shop4.x-1;i++){
                for(int j=i+1;j<shop4.x;j++){
                    if(shop4.score[i]<shop4.score[j]){
                        float tmp1=shop4.score[i];
                        shop4.score[i]=shop4.score[j];
                        shop4.score[j]=tmp1;
                        String s=shop4.info[i];
                        shop4.info[i]=shop4.info[j];
                        shop4.info[j]=s;
                        int tmp2=shop4.price[i];
                        shop4.price[i]=shop4.price[j];
                        shop4.price[j]=tmp2;
                    }
                }
            }
        }
    }
    public static List get(){
        shopList.add(shop1);
        shopList.add(shop2);
        shopList.add(shop3);
        shopList.add(shop4);
        return shopList;
    }
    public static void getAddress(){
        for(int i=0;i<shop1.x;i++){
            String[] str=shop1.info[i].split(",");
            shop1.address[i]=str[1].substring(0,2);
            shop1.name[i]=str[0];
        }
        for(int i=0;i<shop2.x;i++){
            String[] str=shop2.info[i].split(",");
            shop2.address[i]=str[1].substring(0,2);
            shop2.name[i]=str[0];
        }
        for(int i=0;i<shop3.x;i++){
            String[] str=shop3.info[i].split(",");
            shop3.address[i]=str[1].substring(0,2);
            shop3.name[i]=str[0];
        }
        for(int i=0;i<shop4.x;i++){
            String[] str=shop4.info[i].split(",");
            shop4.address[i]=str[1].substring(0,2);
            shop4.name[i]=str[0];
        }

    }
    public static void main(String[] args){
        try{
            String inputPath="D:\\IDEA2019\\IdeaProject\\Teamcoding\\src\\input.csv";
            File file=new File(inputPath);
            BufferedReader bufferedReader=
                    new BufferedReader(new InputStreamReader(new FileInputStream(file)));
            String str;
            shop1.type=1;
            shop2.type=2;
            shop3.type=3;
            shop4.type=4;
            int xx=0;
            while((str=bufferedReader.readLine())!=null){
                xx++;
                if(xx==1)continue;
                //System.out.println(str);
                int x=0;
                int g=0;
                int flag=0;
                for(int i=str.length()-1;i>=0;i--) {
                    if (str.charAt(i) == ',') {
                        x++;
                        if (x == 4) {
                            g=i;
                            flag=i;
                            break;
                        }
                    }
                }
                float s=0;
                int com=0;
                int p=0;
                int flag1=0;
                for(int i=flag+1;i<str.length();i++){
                    if(str.charAt(i)==','){
                        flag=i;
                        break;
                    }
                    if(str.charAt(i)=='.')
                    {
                        flag1=i;
                        continue;
                    }
                    if(flag1==0){
                        s=s*10+str.charAt(i)-'0';
                    }
                    if(flag1==1){
                        s=s+(str.charAt(1)-'0')*0.1f;
                    }

                }
                for(int i=flag+1;i<str.length();i++){
                    if(str.charAt(i)==','){
                        flag=i;
                        break;
                    }
                        p=p*10+str.charAt(i)-'0';
                }
                for(int i=flag+1;i<str.length();i++){
                    if(str.charAt(i)==','){
                        break;
                    }
                    com=com*10+str.charAt(i)-'0';
                }
                //System.out.println(com);
                if(p<50){
                    shop1.info[shop1.x]=str.substring(6,g);
                    shop1.score[shop1.x]=com;
                    shop1.price[shop1.x++]=p;

                }
                else if(p>=50&&p<100){
                    shop2.info[shop2.x]=str.substring(6,g);
                    shop2.score[shop2.x]=com;
                    shop2.price[shop2.x++]=p;
                }
                else if(p>=100&&p<200){
                    shop3.info[shop3.x]=str.substring(6,g);
                    shop3.score[shop3.x]=com;
                    shop3.price[shop3.x++]=p;
                }
                else if(p>=200){
                    shop4.info[shop4.x]=str.substring(6,g);
                    shop4.score[shop4.x]=com;
                    shop4.price[shop4.x++]=p;
                }
            }
            sort(1);
            sort(2);
            sort(3);
            sort(4);
            getAddress();

//            for(int i=0;i<5;i++)
//            System.out.println(shop1.address[i]);
            for(int i=0;i<5;i++){
                System.out.println(shop1.name[i]+" "+shop1.score[i]+" "+shop1.price[i]);
            }
            System.out.println();
            for(int i=0;i<5;i++){
                System.out.println(shop2.name[i]+" "+shop2.score[i]+" "+shop1.price[i]);
            }
            System.out.println();
            for(int i=0;i<5;i++){
                System.out.println(shop3.name[i]+" "+shop3.score[i]+" "+shop1.price[i]);
            }
            System.out.println();
            for(int i=0;i<5;i++){
                System.out.println(shop4.name[i]+" "+shop4.score[i]+" "+shop1.price[i]);
            }
            System.out.println();
            String outputPath="D:\\IDEA2019\\IdeaProject\\Teamcoding\\src" +
                    "\\output.txt";
            File file1=new File(outputPath);
            BufferedWriter bufferedWriter=
                    new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file1)));
            bufferedWriter.write("50元以下\n");
            for(int i=0;i<5;i++){
                bufferedWriter.write(shop1.name[i]+" "+shop1.score[i]+"\n");
            }
            bufferedWriter.write("50-100元\n");
            for(int i=0;i<5;i++){
                bufferedWriter.write(shop2.name[i]+" "+shop2.score[i]+"\n");
            }
            bufferedWriter.write("100-200元\n");
            for(int i=0;i<5;i++){
                bufferedWriter.write(shop3.name[i]+" "+shop3.score[i]+"\n");
            }
            bufferedWriter.write("200元以上\n");
            for(int i=0;i<5;i++){
                bufferedWriter.write(shop4.name[i]+" "+shop4.score[i]+"\n");
            }
            bufferedWriter.flush();
            bufferedWriter.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }


}
