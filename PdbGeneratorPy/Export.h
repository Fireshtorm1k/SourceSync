#pragma once

#include "ComplexType.h"
#include "StructEnumData.h"
#include "PEData.h"
#include "FunctionData.h"
#include "SymbolData.h"

#if defined(PDBGENERATORPY_EXPORTS)
    #define PDB_GENERATOR_API __declspec(dllexport)
#else
    #define PDB_GENERATOR_API __declspec(dllimport)
#endif


extern "C" PDB_GENERATOR_API void CreatePdbGenerator(const srcsync::ComplexTypesData& ComplexTypes, const srcsync::StructsData& Structs, const srcsync::EnumsData& Enums,
    const srcsync::FunctionsData& FunctionsData, const srcsync::PdbInfo& PdbInfo, const srcsync::SectionsType& Sections,
    const srcsync::PublicSymbolsData& SymbolsData, const srcsync::GlobalSymbolsData& GlobalSymbols, srcsync::CpuArchitectureType ArchType);