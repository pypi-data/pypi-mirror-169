################################################################################
#    (C) Copyright CEA LIST. All Rights Reserved.
#    Contributor(s): N2D2 Team (n2d2-contact@cea.fr)
#
#    This software is governed by the CeCILL-C license under French law and
#    abiding by the rules of distribution of free software. You can use,
#    modify and/or redistribute the software under the terms of the CeCILL-C
#    license as circulated by CEA, CNRS and INRIA at the following URL
#    "http://www.cecill.info".
#
#    As a counterpart to the access to the source code and rights to copy,
#    modify and redistribute granted by the license, users are provided only
#    with a limited warranty and the software's author, the holder of the
#    economic rights, and the successive licensors have only limited
#    liability.
#
#    The fact that you are presently reading this means that you have had
#    knowledge of the CeCILL-C license and that you accept its terms.
################################################################################

cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_BUILD_TYPE_INIT Release)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Add compile time reducer
include("${CMAKE_CURRENT_LIST_DIR}/cmake/cotire.cmake")

project(N3D3)

# Add APPLE/MSVC/WIN32
if(UNIX AND NOT APPLE)
    # add -Werror
    add_compile_options(-Wall -Wextra -fPIC)
endif()

if(APPLE)
    add_compile_options(-fvisibility=hidden -fvisibility-inlines-hidden)
endif()

# Under WIN32, add MINGW too
if(MSVC)
    add_compile_options(/wd4834)
endif()


option(BUILD_LIB    "Build the N3D3 C++ library"    ON)
option(BUILD_TESTS  "Build tests"                   OFF)
option(BUILD_DOCS   "Build documentation"           OFF)


if(BUILD_LIB)
    add_subdirectory(${CMAKE_SOURCE_DIR}/n3d3/_libN3D3)
endif()

if(BUILD_DOCS)
    add_subdirectory(${CMAKE_SOURCE_DIR}/docs)
endif()

if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(${CMAKE_SOURCE_DIR}/tests/libN3D3)
endif()
