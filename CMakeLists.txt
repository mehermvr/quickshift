# min version is high to not deal with fetch content backcompat shenanigans.
# this project is not meant as a standalone cpp build anyways and will always be
# built by scikit-build-core as it stands. and scikit-build-core can fetch cmake
# 3.28 if that is the needed version defined in the pyproject.toml
cmake_minimum_required(VERSION 3.28)
project(
  quickshift
  VERSION 0.0.1
  LANGUAGES CXX)

# Set a default build type if none was specified
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  message(
    STATUS "Setting build type to 'RelWithDebInfo' as none was specified.")
  set(CMAKE_BUILD_TYPE RelWithDebInfo)
endif()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_subdirectory(cpp)
