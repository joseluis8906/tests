#ifndef CDI_HPP
#define CDI_HPP

#include <cppcms/application.h>
#include <cppcms/service.h>
#include <cppcms/http_response.h>
#include <cppcms/url_dispatcher.h>
#include <cppcms/url_mapper.h>
#include <cppcms/applications_pool.h>
#include <cppcms/http_request.h>

#include <cppdb/frontend.h>
#include <iostream>
#include <stdlib.h>

class cdi : public cppcms::application 
{
	cppdb::session sql;
  
public:
	
	cdi (cppcms::service &srv);
	void home ();
};

#endif
