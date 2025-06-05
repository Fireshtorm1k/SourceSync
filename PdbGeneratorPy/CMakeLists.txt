cmake_minimum_required(VERSION 3.11)

set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

list(APPEND CMAKE_PREFIX_PATH "${CMAKE_SOURCE_DIR}/extern/pybind11/")
message(STATUS ${CMAKE_PREFIX_PATH})
find_package(LLVM REQUIRED CONFIG)
llvm_map_components_to_libnames(llvm_libs core support DebugInfoPDB)

find_package(pybind11 REQUIRED)

find_package(Python3 REQUIRED COMPONENTS Development)

add_definitions(/bigobj)
add_library(PdbGeneratorPy SHARED)

target_link_libraries(PdbGeneratorPy PRIVATE ${llvm_libs})
target_link_libraries(PdbGeneratorPy PRIVATE Python3::Python)

target_compile_definitions(PdbGeneratorPy PRIVATE PDBGENERATORPY_EXPORTS)

target_include_directories(PdbGeneratorPy PRIVATE ${LLVM_INCLUDE_DIRS})
target_include_directories(PdbGeneratorPy PRIVATE ${pybind11_INCLUDE_DIRS})

target_sources(PdbGeneratorPy PRIVATE ComplexType.h FunctionData.h PdbGenerator.cpp PdbGenerator.h PEData.h PyBindings.cpp StructEnumData.h SymbolData.h TpiBuilder.cpp TpiBuilder.h Export.cpp Export.h)

add_executable(Test test.cpp)

target_link_libraries(Test PUBLIC PdbGeneratorCMake)