import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BusinessCircle {
    public static Map<String,Integer> map=new HashMap<>();
    public static String[] businessName=new String[10000];
    public static int[] score=new int[10000];
    public static int tmp=0;
    public static void sort(){
        for(int i=0;i<tmp-1;i++){
            for(int j=i+1;j<tmp;j++){
                if(score[i]<score[j]){
                    int x=score[i];
                    score[i]=score[j];
                    score[j]=x;
                    String ss=businessName[i];
                    businessName[i]=businessName[j];
                    businessName[j]=ss;
                }
            }
        }
    }
    public static void main(String[] args){

        try{
            String inputPath="D:\\IDEA2019\\IdeaProject\\Teamcoding\\src\\input.csv";
            File file=new File(inputPath);
            BufferedReader bufferedReader=
                    new BufferedReader(new InputStreamReader(new FileInputStream(file)));
            String str;
            int xx=0;
            while((str=bufferedReader.readLine())!=null) {
                xx++;
                if(xx==1)continue;
                int flag=0;
                int tot=0;
                for(int i=str.length()-1;i>=0;i--){
                    if(str.charAt(i)==','){
                        tot++;
                    }
                    if(tot==2){
                        flag=i;
                        break;
                    }
                }
                for(int i=flag+1;i<str.length();i++){
                    if(str.charAt(i)==','){
                        flag=i;
                        break;
                    }
                    tot=tot*10+str.charAt(i)-'0';
                }
                String name=str.substring(flag+1,str.length());
                if(map.get(name)==null){
                    map.put(name,tmp);
                    score[tmp]+=tot;
                    businessName[tmp]=name;
                    tmp++;
                }
                else{
                    score[map.get(name)]+=tot;
                }
            }
            sort();
//            for(int i=0;i<tmp;i++){
//                System.out.println(businessName[i]+" "+score[i]);
//            }
            String outputPath="D:\\IDEA2019\\IdeaProject\\Teamcoding\\src" +
                    "\\output1.txt";
            File file1=new File(outputPath);
            BufferedWriter bufferedWriter=
                    new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file1)));
            for(int i=0;i<5;i++){
                bufferedWriter.write(businessName[i]+" "+score[i]+"\n");
            }
            bufferedWriter.flush();
            bufferedWriter.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }


}
