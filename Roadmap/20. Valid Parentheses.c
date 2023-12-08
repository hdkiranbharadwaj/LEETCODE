struct stk{
    char item[5000];
    int top;
};
typedef struct stk STK;
void push(char c, STK *S)
{  
    S->top=S->top+1;
    S->item[S->top] = c;
}
char pop(STK *S)
{
    return(S->item[S->top--]);
}
bool isValid(char * s){
    char c,k;
    STK S;
    S.top=-1;
    while((c=*(s++))!='\0')
    {   
        if(c=='('||c=='{'||c=='[')
           {push(c,&S);}
        else if(c==')'||c=='}'||c==']')
          { 
              if(S.top==-1)
              {
                  return false;
              }
              k=pop(&S);
              switch(k)
              {
               case '(':if(c!=')')
                            return false;
                            break;
               case '{':if(c!='}')
                            return false;
                            break;
               case '[':if(c!=']')
                            return false;
                            break;
              }
          }
        
    }
    if(S.top!=-1)
    return false;
    return true;
}


