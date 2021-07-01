class Obj{
    String word;
    int len;
    Obj (String word, int len){
        this.word=word;
        this.len=len;
    }
}
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (beginWord.length() ==0 || endWord.length() ==0 || wordList.size()==0)
            return 0;
        
        Queue<Obj> q= new LinkedList<>();
        q.add(new Obj(beginWord, 1));
        while(!q.isEmpty()){
            Obj curr=q.poll();
            ListIterator<String> itr=wordList.listIterator();
            while(itr.hasNext()){
                String temp=itr.next();
                if(isAdjacent(curr.word, temp)){
                    itr.remove();
                    q.add(new Obj(temp, curr.len+1));
                    if(temp.equals(endWord))
                        return curr.len+1;
                        
                }
                
            }
        }
        return 0;
    }
public boolean isAdjacent(String s1, String s2){
    int count=0;
    for(int i=0; i<s1.length();i++){
        if(s1.charAt(i)!=s2.charAt(i)){
            count++;
            if(count>1)
                return false;
        }
    }
        return count>1?false:true;
    }
}
