library(biomaRt)
mart <- useEnsembl(biomart = "ensembl", dataset = "hsapiens_gene_ensembl")

## Code for part i) of the question

v <- c()
for (variable in 1:22) {
  k <- (dim(getBM(mart = mart, attributes = "ensembl_gene_id", filters = "chromosome_name", values = as.character(variable))))
  v <- c(v, k[1])
}

chromosome_x <- dim(getBM(mart = mart, attributes = "ensembl_gene_id", filters = "chromosome_name", values = "X"))
chromosome_y <- dim(getBM(mart = mart, attributes = "ensembl_gene_id", filters = "chromosome_name", values = "Y"))

v <- c(v, chromosome_x[1])
v <- c(v, chromosome_y[1])

for (i in 1:22) {
  print(paste("No of genes on chromosome", i, v[i]))
}
print(paste("No of genes on chromosome X", v[23]))
print(paste("No of genes on chromosome Y", v[24]))

## Code for part ii) of the question
print(paste("Sum total of all the genes", sum(v)))

##From the above code, we observe that chromosome 1 has the maximum amount of genes i.e. 5557

#Store all gene ids in 'genes' variable for chromosome 1
genes <- getBM(attributes = "external_gene_name", filters = "chromosome_name", values = "1", mart = mart)

#Finding number of transcripts by iterating over all genes and finding their 'transcript_count'
#also finding gene with max no of transcripts and transcript having maximum length

max_transcripts <- getBM(attributes="transcript_count", values = genes[1,], mart = mart,filters = "external_gene_name")[[1]]
no_of_transcripts <- max_transcripts
max_transcripts_index <- 1
longest_tr <- max(getBM(attributes="transcript_length", values = genes[1,], mart = mart,filters = "external_gene_name"))
longest_tr_idx <- 1
for (i in 2:dim(genes)) {
  n <- max(getBM(attributes="transcript_count", values = genes[i,], mart = mart,filters = "external_gene_name"))
  tr_length <- max(getBM(attributes="transcript_length", values = genes[i,], mart = mart,filters = "external_gene_name"))
  no_of_transcripts = no_of_transcripts + n[[1]]
  
  #Checking for max no of transcripts
  if (n > max(max_transcripts)){
    max_transcripts=n
    max_transcripts_index=i
  }
  
  #Checking for max length of transcripts
  if(tr_length > longest_tr){
    longest_tr = tr_length
    longest_tr_idx = i
  }
  
}
print(paste("Total no of transcripts on chromosome 1:", no_of_transcripts))
print(paste("Gene having max no of transcripts: ", genes[max_transcripts_index, ]))
print(paste("Transcript having maximum length: ", getBM(attributes="ensembl_transcript_id", values = genes[longest_tr_idx,], mart = mart,filters = "external_gene_name")))



