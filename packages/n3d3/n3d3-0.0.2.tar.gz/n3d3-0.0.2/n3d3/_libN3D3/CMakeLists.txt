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


option(CORE         "core"              ON)
option(DATAPROVIDER "data provider "    ON)
option(PYBIND       "python binding"    ON)
option(TRANSMITTERS "transmitters"      ON)

add_library(n3d3_lib STATIC)

# Add include directories 
target_include_directories(n3d3_lib PUBLIC "include")

# Mandatory libraries
find_package(Threads REQUIRED)
target_link_libraries(n3d3_lib PUBLIC Threads::Threads)

# Containers module
file(GLOB_RECURSE containers_src_files "src/containers/*.cpp")
target_sources(n3d3_lib PRIVATE ${containers_src_files})

# Utils module
file(GLOB_RECURSE containers_src_files "src/utils/*.cpp")
target_sources(n3d3_lib PRIVATE ${containers_src_files})

# Core module
if(CORE)
    message(STATUS "Core enabled")
endif()


if (PYBIND)
    message(STATUS "Using third_party/pybind11 for Python binding")
    add_subdirectory(${CMAKE_SOURCE_DIR}/third_party/pybind11 ${CMAKE_BINARY_DIR}/pybind11)

    # Check if third_party/pybind11 can be used for binding
    if (NOT EXISTS "${CMAKE_SOURCE_DIR}/third_party/pybind11/CMakeLists.txt")
      message(FATAL_ERROR
      "Cannot find third_party/pybind11 directory that's needed to "
      "build libN3D3. If you use git, make sure you have cloned submodules:\n"
      "  git submodule update --init --recursive\n")
    endif()

    file(GLOB_RECURSE pybind_src_files "python_binding/*.cpp")
    pybind11_add_module(libN3D3 MODULE ${pybind_src_files})
    target_include_directories(libN3D3 PUBLIC ${pybind11_INCLUDE_DIRS} "python_binding")
    target_link_libraries(libN3D3 PUBLIC n3d3_lib)
endif()


# Activate compile time reducer for n3d3_lib
set_target_properties(n3d3_lib PROPERTIES COTIRE_ADD_UNITY_BUILD FALSE)
set_target_properties(n3d3_lib PROPERTIES COTIRE_CXX_PREFIX_HEADER_INIT "include/utils/Precompiled.hpp")
cotire(n3d3_lib)