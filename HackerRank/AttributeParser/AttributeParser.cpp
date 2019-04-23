//
// Abdulrahman Alattas
// Apr 20-21, 2019
// Time: 4 Hour 
// 
// Solution for:
// https://www.hackerrank.com/challenges/attribute-parser/problem
//
//
// TODO:
// - attribute value without (") ex: <tag2 size = 45>
//
//


#include <string>
#include <iostream>
#include <map>
using namespace std;


// a tag children list is a map of string to tag* (tag name to tag pointer)
class tag;      // early signature for the typedef command
typedef map<string, tag*> tagChildMap;      // Tag Children Map
// an attribute list is a map of string to string (key to vlaue)
typedef map<string, string> atrsMap;        // Attributes Map


// could be a struct but a class leave the option for adding methods such as printAttributes()
class tag{
    public:
        string name;
        atrsMap attributes;
        tag* parent;
        tagChildMap children;
};


// given a line of source code and its tag node, add the attributes to its attributes list
// attributes are a map<string(key), string(value)>
void readTagAttributes(const string line, tag* newTag){
    size_t strI = 0;
    // get the index right after the tag name (skip to the attributes)
    while (line[strI] != '<') strI++;       // skip indentation
    strI++;
    while (line[strI] == ' ') strI++;       // skip spaces between < and the tag name
    while (line[strI] != ' ' && line[strI] != '>') strI++;       // skip tag name

    while (true){
        size_t tokenStart, tokenLen;

        // chek end of tag
        while (line[strI] == ' ') strI++;
        if (line[strI] == '>') break;

        // get attribute name
        while (line[strI] == ' ') strI++;       // never runs
        tokenStart = strI;
        tokenLen = 0;
        while (line[strI] != ' ' && line[strI] != '=') strI++;
        tokenLen = strI - tokenStart;
        string key = line.substr(tokenStart, tokenLen);

        // get attribute value
        while (line[strI] != '"') strI++;
        tokenStart = ++strI;
        tokenLen = 0;
        while (line[strI] != '"') strI++;
        tokenLen = strI - tokenStart;
        string value = line.substr(tokenStart, tokenLen);

        // increment strI to after the close "
        strI++;

        // save attribute
        newTag->attributes[key] = value;
    }
}


// given a source code and the number of lines, 
// build a tag tree and return a pointer to the tree root tag
tag* buildTagTree(const string source[], int N){
    tag* root = new tag;
    root->name = "root";
    root->parent = nullptr;
    tag* currentParent = root;
    for (int i=0; i<N; i++){
        string line = source[i];

        // get indecies for the start and len of tag name
        size_t strI = 0, tokenStart, tokenLen;   // indecies for the begin and len of the token
        while (line[strI] != '<') strI++;       // skip indentation
        if (line.substr(strI, 2) != "</"){       // check line is not close tag
            // get the tag name
            strI++;
            while (line[strI] == ' ') strI++;
            tokenStart = strI;
            tokenLen = 0;
            while (line[strI] != ' ' && line[strI] != '>') strI++;
            tokenLen = strI - tokenStart;

            tag *newTag = new tag;
            newTag->name = line.substr(tokenStart, tokenLen);
            readTagAttributes(line, newTag);
            newTag->parent = currentParent;          
            currentParent->children[newTag->name] = newTag;     // add it to its parent children list
            currentParent = newTag;         // update current parent
        }else{
            // source line is a close tag, update current parent
            currentParent = currentParent->parent;
        }
    }
    return root;
}


void printResult(const string query[],const int Q, tag* root){
    for (int i=0; i<Q; i++){
        tag* currentTag = root;
        string line = query[i];
        size_t strI = 0, tokenStart, tokenLen;

        // find the queried tag node
        while (true){          // going down the tree at each iteration
            tokenStart = strI;
            while (line[strI] != '.' && line[strI] != '~') strI++;
            tokenLen = strI - tokenStart;
            string tagName = line.substr(tokenStart, tokenLen);
            if (currentTag->children.count(tagName)){       // check child exist 
                tag* childTag = currentTag->children[tagName];
                currentTag = childTag;
            }else
                break;
            if (line[strI++] == '~') break;
        }


        // get the queried attribute name
        string atrName = line.substr(strI);

        if (currentTag->attributes.count(atrName))       // check attribute exist 
            cout << currentTag->attributes[atrName] << endl;
        else
            cout << "Not Found!" << endl;

    }
}


int main() {

    // get N and Q
    int N, Q;
    cin >> N; 
    cin >> Q;
    cin.ignore();

    // get source lines
    string source[N];
    for (int i=0; i<N; i++){
        getline(cin, source[i]);
    }

    // get query lines
    string query[Q];
    for (int i=0; i<Q; i++){
        getline(cin, query[i]);
    }

    // build a source tree and return the root tag node
    tag* root = buildTagTree(source, N);

    // print results requested by the queries
    printResult(query, Q, root);

    return 0;
}

