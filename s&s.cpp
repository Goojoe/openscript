#include<iostream>
using namespace std;
/*************************************
*this is a practice                  *
*begining from double link           *
*maybe i will add some algorithm     *
*just for fun and for my boring time *
*************************************/
#include<iostream>
#include<cmath>
using namespace std;
class node {
	public:
		int data;
		node *pre;
		node *next;
};
class tnode {//树的节点
	public:
		int index;
		node  *p;
		tnode *l = NULL;
		tnode *r = NULL;
};
class tree {//此树用来优化搜索为O(log2(n))
		tnode *head = new tnode;
		void create(int step, tnode *point) {
			if (step == 0) {
				return;
			}
			point->r = new tnode;
			point->l = new tnode;
			if (step == 1) {
				point->r->r = NULL;
				point->r->l = NULL;
				point->l->r = NULL;
				point->l->l = NULL;
			}
			point->r->index = point->index;
			point->l->index = point->index - pow(2, step - 1);
			create(step - 1, point->l);
			create(step - 1, point->r);
		}
		tnode *find(int n, tnode *point) {
			if (n == point->index) {
				return point;
			}
			if (n > point->l->index) {
				find(n, point->r);
			} else {
				find(n, point->l);
			}
		}
	public:
		void start(int n) {
			int step = log(n) / log(2) + 1;
			head->index = pow(2, step);
			//cout << step;
			create(step, head);
		}
		tnode *f(int n) {
			return find(n, head);
		}
};
class d_link {
		node *head = new node;
		node *tail = new node;
		tree quick_find;
		int lenth = 0;
		bool planted;//若进行增删记得调整此项
	public:
		void start(int n) {
			quick_find.start(n);
			lenth = n;
			tnode *temp_point = new tnode;
			head->pre = NULL;
			tail->next = NULL;
			node *point = new node;
			head->next = point;
			point->pre = head;
			for (int i = 1; i <= n; i++) {
				temp_point = quick_find.f(i);
				temp_point->p = point;
				//cin>>point->data;
				point->data = i;
				node *temp = new node;
				point->next = temp;
				temp->pre = point;
				point = temp;
			}
			tail = point;
			planted = 1;
		}
		void re_plant() {
			quick_find.start(lenth);
			node *point = head->next;
			tnode *temp_point = new tnode;
			for (int i = 1; i <= lenth; i++) {
				temp_point = quick_find.f(i);
				temp_point->p = point;
				point = point->next;
			}
			planted = 1;
		}
		node *find(int index) {
			if (planted) {
				tnode *temp_point = quick_find.f(index);
				return temp_point->p;
			} else {
				re_plant();
				tnode *temp_point = quick_find.f(index);
				return temp_point->p;
			}
		}
		void insert(int index, int x) {
			node *point1 = head->next;
			point1 = find(index);
			node *point2 = point1->next;
			node *temp = new node;
			temp->data = x;
			point1->next = temp;
			temp->pre = point1;
			temp->next = point2;
			point2->pre = temp;
			planted = 0;
		}
		bool is_emp() {
			if (head->next == tail) {
				return true;
			} else {
				return false;
			}
		}
		bool is_inc() {
			node *point = head->next;
			bool cheak = true;
			while (point != tail) {
				if ((point->next->data) < (point->data)) {
					cheak = !cheak;
					break;
				}
			}
			return cheak;
		}
		void putout() {
			node *point = head->next;
			while (point != tail) {
				cout << point->data << endl;
				point = point->next;
			}
		}
		void reverse_putout() {
			node *point = tail->pre;
			while (point != head) {
				cout << point->data << endl;
				point = point->pre;
			}
		}
		int get_first() {
			return head->next->data;
		}
		void del_first() {
			if (!is_emp()) {
				node *temp = head->next->next;
				head->next = temp;
				temp->pre = head;
			}
			planted = 0;
		}
		int get_last() {
			return tail->pre->data;
		}
		void del_last() {
			if (!is_emp()) {
				node *temp = tail->pre->pre;
				tail->pre = temp;
				temp->next = tail;
			}
			planted = 0;
		}
		void append(int x) {
			node *temp = new node;
			node *point = tail->pre;
			point->next = temp;
			temp->pre = point;
			temp->next = tail;
			tail->pre = temp;
			temp->data = x;
			planted = 0;
		}
		void del(int index) {
			node *point = head->next;
			for (int i = 1; i <= index - 1; i++) {
				point = point->next;
			}
			node *temp1 = point->pre;
			node *temp2 = point->next;
			temp1->next = temp2;
			temp2->pre = temp1;
			planted = 0;
		}
};
class stack {
		d_link s;
		int lenth = 0;
	public:
		void start() {
			s.start(0);
		}
		void push(int n) {
			s.append(n);
			lenth++;
		}
		int get_lenth() {
			return lenth;
		}
		int pop() {
			int temp = s.get_last();
			s.del_last();
			lenth--;
			return temp;
		}
};
class queue {
		d_link q;
		int lenth = 0;
	public :
		void start() {
			q.start(0);
		}
		int get_lenth() {
			return lenth;
		}
		void push(int x) {
			q.append(x);
			lenth++;
		}
		int pop() {
			int temp = q.get_first();
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
