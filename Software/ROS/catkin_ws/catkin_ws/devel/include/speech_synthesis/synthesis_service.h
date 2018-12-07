// Generated by gencpp from file speech_synthesis/synthesis_service.msg
// DO NOT EDIT!


#ifndef SPEECH_SYNTHESIS_MESSAGE_SYNTHESIS_SERVICE_H
#define SPEECH_SYNTHESIS_MESSAGE_SYNTHESIS_SERVICE_H

#include <ros/service_traits.h>


#include <speech_synthesis/synthesis_serviceRequest.h>
#include <speech_synthesis/synthesis_serviceResponse.h>


namespace speech_synthesis
{

struct synthesis_service
{

typedef synthesis_serviceRequest Request;
typedef synthesis_serviceResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct synthesis_service
} // namespace speech_synthesis


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::speech_synthesis::synthesis_service > {
  static const char* value()
  {
    return "d5bb794ce9c6117c55c80145b1c203b2";
  }

  static const char* value(const ::speech_synthesis::synthesis_service&) { return value(); }
};

template<>
struct DataType< ::speech_synthesis::synthesis_service > {
  static const char* value()
  {
    return "speech_synthesis/synthesis_service";
  }

  static const char* value(const ::speech_synthesis::synthesis_service&) { return value(); }
};


// service_traits::MD5Sum< ::speech_synthesis::synthesis_serviceRequest> should match 
// service_traits::MD5Sum< ::speech_synthesis::synthesis_service > 
template<>
struct MD5Sum< ::speech_synthesis::synthesis_serviceRequest>
{
  static const char* value()
  {
    return MD5Sum< ::speech_synthesis::synthesis_service >::value();
  }
  static const char* value(const ::speech_synthesis::synthesis_serviceRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::speech_synthesis::synthesis_serviceRequest> should match 
// service_traits::DataType< ::speech_synthesis::synthesis_service > 
template<>
struct DataType< ::speech_synthesis::synthesis_serviceRequest>
{
  static const char* value()
  {
    return DataType< ::speech_synthesis::synthesis_service >::value();
  }
  static const char* value(const ::speech_synthesis::synthesis_serviceRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::speech_synthesis::synthesis_serviceResponse> should match 
// service_traits::MD5Sum< ::speech_synthesis::synthesis_service > 
template<>
struct MD5Sum< ::speech_synthesis::synthesis_serviceResponse>
{
  static const char* value()
  {
    return MD5Sum< ::speech_synthesis::synthesis_service >::value();
  }
  static const char* value(const ::speech_synthesis::synthesis_serviceResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::speech_synthesis::synthesis_serviceResponse> should match 
// service_traits::DataType< ::speech_synthesis::synthesis_service > 
template<>
struct DataType< ::speech_synthesis::synthesis_serviceResponse>
{
  static const char* value()
  {
    return DataType< ::speech_synthesis::synthesis_service >::value();
  }
  static const char* value(const ::speech_synthesis::synthesis_serviceResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // SPEECH_SYNTHESIS_MESSAGE_SYNTHESIS_SERVICE_H