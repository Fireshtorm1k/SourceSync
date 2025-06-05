#pragma once
#include "PdbGenerator.h"
#include "Export.h"
using namespace srcsync;

PdbGenerator* pdbGenerator;

extern "C" PDB_GENERATOR_API void CreatePdbGenerator(const ComplexTypesData& ComplexTypes, const StructsData& Structs, const EnumsData& Enums,
    const FunctionsData& FunctionsData, const PdbInfo& PdbInfo, const SectionsType& Sections,
    const PublicSymbolsData& SymbolsData, const GlobalSymbolsData& GlobalSymbols, CpuArchitectureType ArchType) {
    pdbGenerator = new PdbGenerator(ComplexTypes, Structs, Enums, FunctionsData, PdbInfo, Sections, SymbolsData, GlobalSymbols, ArchType);
}