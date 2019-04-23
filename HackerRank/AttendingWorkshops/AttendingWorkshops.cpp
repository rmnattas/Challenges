#include <iostream>
#include <list>
using namespace std;


struct Workshop{
    int start, duration, end;
};


struct Available_Workshops{
    int n;
    list<Workshop> workshops;
};

bool compEndWorkshops (Workshop ws1, Workshop ws2){
    return ws1.end < ws2.end;
}

Available_Workshops* initialize (int start_time[], int duration[], int n){
    Available_Workshops* availableWorkshops = new Available_Workshops;
    availableWorkshops->n = 0;
    
    for (int i=0; i<n; i++){
        Workshop ws = {start_time[i], duration[i], (start_time[i]+duration[i]) };
        availableWorkshops->workshops.push_back(ws);
        availableWorkshops->n++;
    }

    return availableWorkshops;
}


int CalculateMaxWorkshops(Available_Workshops* ptr){
    ptr->workshops.sort(compEndWorkshops);

    int N = 0, lastEnd = 0;
    for (Workshop ws : ptr->workshops){
       if (ws.start >= lastEnd){
           N++;
           lastEnd = ws.end;
       }
    }
    
    return N;
}


int main(int argc, char *argv[]){
    
    int N;
    cin >> N;
    cin.ignore();

    int start[N];
    for (int i=0; i<N; i++)
        cin >> start[i];
    cin.ignore();

    int duration[N];
    for (int i=0; i<N; i++)
        cin >> duration[i];
    cin.ignore();

    Available_Workshops* avws = initialize(start, duration, N);
    cout << CalculateMaxWorkshops(avws) << endl;

    return 0;
}

