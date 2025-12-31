cmake_minimum_required(VERSION 3.20)
project(mylib C)

add_library(mylib SHARED
  src/mylib.c
)

target_include_directories(mylib PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_compile_definitions(mylib PRIVATE MYLIB_BUILDING)

set_target_properties(mylib PROPERTIES
  OUTPUT_NAME "mylib"
)

# ---- install layout: dist/bin + dist/include ----
install(TARGETS mylib
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION bin
  ARCHIVE DESTINATION lib
)

install(FILES
  ${CMAKE_CURRENT_SOURCE_DIR}/include/mylib.h
  DESTINATION include
)
