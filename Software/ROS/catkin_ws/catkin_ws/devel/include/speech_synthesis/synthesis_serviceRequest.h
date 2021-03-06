// Generated by gencpp from file speech_synthesis/synthesis_serviceRequest.msg
// DO NOT EDIT!


#ifndef SPEECH_SYNTHESIS_MESSAGE_SYNTHESIS_SERVICEREQUEST_H
#define SPEECH_SYNTHESIS_MESSAGE_SYNTHESIS_SERVICEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace speech_synthesis
{
template <class ContainerAllocator>
struct synthesis_serviceRequest_
{
  typedef synthesis_serviceRequest_<ContainerAllocator> Type;

  synthesis_serviceRequest_()
    : req()  {
    }
  synthesis_serviceRequest_(const ContainerAllocator& _alloc)
    : req(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _req_type;
  _req_type req;





  typedef boost::shared_ptr< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> const> ConstPtr;

}; // struct synthesis_serviceRequest_

typedef ::speech_synthesis::synthesis_serviceRequest_<std::allocator<void> > synthesis_serviceRequest;

typedef boost::shared_ptr< ::speech_synthesis::synthesis_serviceRequest > synthesis_serviceRequestPtr;
typedef boost::shared_ptr< ::speech_synthesis::synthesis_serviceRequest const> synthesis_serviceRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace speech_synthesis

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b8dc53fbc3707f169aa5dbf7b19d2567";
  }

  static const char* value(const ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb8dc53fbc3707f16ULL;
  static const uint64_t static_value2 = 0x9aa5dbf7b19d2567ULL;
};

template<class ContainerAllocator>
struct DataType< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "speech_synthesis/synthesis_serviceRequest";
  }

  static const char* value(const ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string req\n\
";
  }

  static const char* value(const ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.req);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct synthesis_serviceRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::speech_synthesis::synthesis_serviceRequest_<ContainerAllocator>& v)
  {
    s << indent << "req: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.req);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SPEECH_SYNTHESIS_MESSAGE_SYNTHESIS_SERVICEREQUEST_H
