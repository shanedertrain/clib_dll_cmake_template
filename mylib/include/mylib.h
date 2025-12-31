#pragma once

#include <stdint.h>

#if defined(_WIN32)
  #if defined(MYLIB_BUILDING)
    #define MYLIB_API __declspec(dllexport)
  #else
    #define MYLIB_API __declspec(dllimport)
  #endif
  #define MYLIB_CALL __cdecl
#else
  #if defined(MYLIB_BUILDING)
    #define MYLIB_API __attribute__((visibility("default")))
  #else
    #define MYLIB_API
  #endif
  #define MYLIB_CALL
#endif

#ifdef __cplusplus
extern "C" {
#endif

MYLIB_API int32_t MYLIB_CALL mylib_add_i32(int32_t a, int32_t b);

#ifdef __cplusplus
}
#endif
