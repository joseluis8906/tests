#include <cppsp/page.H>
#include <cpoll/cpoll.H>
#include <cppsp/common.H>
#include <cppsp/stringutils.H>
#include <rgc.H>
using namespace cppsp;
using namespace CP;
#line 2

#include <zdb/zdb.h>
//example cppsp module that rewrites all urls to /100.html, and treats it as
//a dynamic page

static URL_T url = URL_new ("postgresql://localhost:5432/cdi?user=joseluis&password=joseluis890609");
static ConnectionPool_T pool = ConnectionPool_new (url);

DelegateChain<void(Request&, Response&, Delegate<void()>)>::item* it;
Server* server;
void handleRequest(void*, Request& req, Response& resp, Delegate<void()> cb) 
{
        cppsp::String path = req.path;
        
        if (path == "/") 
        {
            resp.headers["Content-type"] = "text/plain";
            
            Connection_T conn = ConnectionPool_getConnection (pool);
            TRY
            {
                ResultSet_T r = Connection_executeQuery (conn, "SELECT version();");
                while (ResultSet_next (r))
                {
                    string message = ResultSet_getString (r,1);
                    resp.write (message);
                    break;
                }
                
            }
            CATCH (SQLException)
            {
                resp.write (Exception_frame.message);
            }
            FINALY
            {
                Connection_close (conn);
            }
            END_TRY;
            
            server->handleDynamicRequest ("/central/index.cppsp",req,resp,cb);            
        }
        else if (path == "/open_pool") 
        { 
            ConnectionPool_start (pool);
            server->handleDynamicRequest ("/central/open_pool.cppsp",req,resp,cb);
        }
        else if (path == "/close_pool") 
        { 
            ConnectionPool_free (&pool);
            URL_free (&url);
            server->handleDynamicRequest ("/central/close_pool.cppsp",req,resp,cb);
        }
        else {server->handleDynamicRequest("/404.cppsp",req,resp,cb);}
        
}
extern "C" void initModule(Server* s) 
{       
        server=s;
	it=s->handleRequest.attach(&handleRequest);
}
extern "C" void deinitModule() 
{
	server->handleRequest.detach(it);
}
class __cppsp_unnamed_page: public Page {
public:
virtual void render(StreamWriter& output) override {
}
};
extern "C" int getObjectSize() {return sizeof(__cppsp_unnamed_page);}
extern "C" Page* createObject(void* mem) {if(mem==NULL) return new __cppsp_unnamed_page(); else return new (mem) __cppsp_unnamed_page();}
extern "C" Page* createObject1(RGC::Allocator* alloc) {__cppsp_unnamed_page* tmp = new (alloc->alloc(sizeof(__cppsp_unnamed_page))) __cppsp_unnamed_page(); tmp->allocator=alloc; return tmp;}
