# Heuristic:

* using a header-txt.txt as input, group headers using anchor keywords

  - keywords are targeting specific types of information:
  
    kw = `primer` to cluster information about nucleic acid probes -
      -> tables found in `Material & Method` Tables.
      
    kw = `{pval, p-value, p, mean ± SEM, etc.. }`
      -> tables found in 'Results` or `Discussion`
  
  - following clustering of headers based on 'seed keywords', inspect the collection of headers
  
    -identify qualifiers
        (e.g. if `primer` present, is there an attribute such as 'orientation', 'length'
      
    - identify associated entities 
        (e.g. if `p-value` present, is there a statistical test present:[anova, t-test...]
        
    - identify the header containing most field in an attempt to identify the most exhaustive sets of attributes for a domain
    
    - use this set to build an exemplar / canonical table and derived the Frictionless Data Package from it
    
    - edit the Frictionless JSON to:
    
      - add `field definition`
      
      - assign an `rdfType` -> suggestion to uses OBO Foundry resources such as [GO](), [So](), [STATO]()
      
 # Results:
 
 * identification on several salient patterns:
  
    - PCR primer information: e.g.   [‘Gene’, ‘Species’, ‘Forward primer (5’−3’)’, ‘Reverse primer (5’−3’)’]

    - Antibody information: e.g.  ['Antibody', 'Source', 'Company', 'Catalog number', 'Dilutions used']
    
    - RNAi information: ['RNAi Lines', 'Source', 'Stock number', 'Insertion site', 'Vector:', 'Other info:']

    - Reagents in General: ['Reagent', 'Type', 'Manufacturer', 'Catalog #', 'Comments']
    
    - Study Design / Factors and Factor levels / 
    
    - Differential analysis
    
    - Enrichment analysis
    
    - Survival Analyslis
    
    - Model/Data Transformation fitness analysis:
    
    - Assay or Technology specific reporting tables:
        
          - Kinetic/Binding/Affinity assay
          - fMRI activation analysis
          - electrophysiology assay

