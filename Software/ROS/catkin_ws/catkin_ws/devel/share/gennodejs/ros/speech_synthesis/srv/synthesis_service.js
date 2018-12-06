// Auto-generated. Do not edit!

// (in-package speech_synthesis.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class synthesis_serviceRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.req = null;
    }
    else {
      if (initObj.hasOwnProperty('req')) {
        this.req = initObj.req
      }
      else {
        this.req = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type synthesis_serviceRequest
    // Serialize message field [req]
    bufferOffset = _serializer.string(obj.req, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type synthesis_serviceRequest
    let len;
    let data = new synthesis_serviceRequest(null);
    // Deserialize message field [req]
    data.req = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.req.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'speech_synthesis/synthesis_serviceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b8dc53fbc3707f169aa5dbf7b19d2567';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string req
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new synthesis_serviceRequest(null);
    if (msg.req !== undefined) {
      resolved.req = msg.req;
    }
    else {
      resolved.req = ''
    }

    return resolved;
    }
};

class synthesis_serviceResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.res = null;
    }
    else {
      if (initObj.hasOwnProperty('res')) {
        this.res = initObj.res
      }
      else {
        this.res = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type synthesis_serviceResponse
    // Serialize message field [res]
    bufferOffset = _serializer.int32(obj.res, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type synthesis_serviceResponse
    let len;
    let data = new synthesis_serviceResponse(null);
    // Deserialize message field [res]
    data.res = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'speech_synthesis/synthesis_serviceResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ca16cfbd5443ad97f6cc7ffd6bb67292';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 res
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new synthesis_serviceResponse(null);
    if (msg.res !== undefined) {
      resolved.res = msg.res;
    }
    else {
      resolved.res = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: synthesis_serviceRequest,
  Response: synthesis_serviceResponse,
  md5sum() { return 'd5bb794ce9c6117c55c80145b1c203b2'; },
  datatype() { return 'speech_synthesis/synthesis_service'; }
};
