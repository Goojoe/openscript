#include<iostream>
using namespace std;
/*************************************
*this is a practice                  *
*begining from double link           *
*maybe i will add some algorithm     *
*just for fun and for my boring time *
*************************************/
class node{
	public:
		int data;
		node *pre;
		node *next;
};
class d_link {
		node *head=new node;
		node *tail=new node;
	public:
		void start(int n){
			head->pre=NULL;
			tail->next=NULL;
			node *point=new node;
			head->next=point;
			point->pre=head;
			for(int i=1;i<=n;i++){
				//cin>>point->data;
				point->data=i;
				node *temp=new node;
				point->next=temp;
				temp->pre=point;
				point=temp;
			}
			tail=point;
		}
		void insert(int index ,int x){
			node *point1=head->next;
			for(int i=0;i<index;i++){
				point1=point1->next;
			}
			node *point2=point1->next;
			node *temp=new node;
			temp->data=x;
			point1->next=temp;
			temp->pre=point1;
			temp->next=point2;
			point2->pre=temp;
		}
		bool is_emp(){
			if(head->next==tail){
				return true;
			}
			else {
				return false;
			}
		}
		bool is_inc(){
			node *point=head->next;
			bool cheak=true;
			while(point!=tail){
				if((point->next->data)<(point->data)){
					cheak=!cheak;
					break;
				}
			}
			return cheak;
		}
		void putout(){
			node *point=head->next;
			while(point!=tail){
				cout<<point->data<<endl;
				point=point->next;
			}
		}
		void reverse_putout(){
			node *point=tail->pre;
			while(point!=head){
				cout<<point->data<<endl;
				point=point->pre;
			}
		}
		int get_first(){
			return head->next->data;
		}
		void del_first(){
			if(!is_emp()){
				node *temp=head->next->next;
				head->next=temp;
				temp->pre=head;
			}
		}
		int get_last(){
			return tail->pre->data;
		}
		void del_last(){
			if(!is_emp()){
				node *temp=tail->pre->pre;
				tail->pre=temp;
				temp->next=tail;
			}
		}
		void append(int x){
			node *temp=new node;
			node *point=tail->pre;
			point->next=temp;
			temp->pre=point;
			temp->next=tail;
			tail->pre=temp;
			temp->data=x;
		}
		void del(int index){
			node *point=head->next;
			for(int i=1;i<=index-1;i++){
				point=point->next;
			}
			node *temp1=point->pre;
			node *temp2=point->next;
			temp1->next=temp2;
			temp2->pre=temp1;
		}
};
class stack {
		d_link s;
		int lenth=0;
	public:
		void start(){
			s.start(0);
		}
		void push(int n) {
			s.append(n);
			lenth++;
		}
		int get_lenth(){
			return lenth;
		}
		int pop(){
			int temp=s.get_last();
			s.del_last();
			lenth--;
			return temp;
		}
};
class queue{
	d_link q;
	int lenth=0;
	public :
		void start(){
			q.start(0);
		}
		int get_lenth(){
			return lenth;
		}
		void push(int x){
			q.append(x);
			lenth++;
		}
		int pop(){
			int temp=q.get_first();
			q.del_first();
			lenth--;
			return temp;
		}
		
};
int main(){
	d_link a;
	a.start(5);
	a.insert(3,3);
	a.putout();
	/*
	int n=10086;
	stack bin;
	bin.start();
	while(n!=0){
		bin.push(n%2);
		n/=2;
	}
	int l=bin.get_lenth();
	for(int i=1;i<=l;i++){
		cout<<bin.pop();
	}*/
	return 0;
}
