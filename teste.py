import pandas as pd
import nlpaug.augmenter.word as naw

def reduz_linhas(db):
    k=len(db)-100

    db = db.drop(db.sample(n=k).index)
    return db

def augment_data(db):
    k = 100 - len(db)

    aug = naw.SynonymAug(aug_src='wordnet', lang='eng')
    
    new_rows=[]
    class_value = db['Classe'].iloc[0]
    print(class_value)
    text_column_index = db.columns.get_loc('Texto Extraído')

    for _ in range(k):
        random_row = db.sample(n=1)

        text = random_row.iloc[0, text_column_index]

        augmented_sentence = aug.augment(text)
        new_rows.append([random_row.iloc[0, 0],augmented_sentence,class_value])

    new_df = pd.DataFrame(new_rows, columns=['Nome do Arquivo', 'Texto Extraído', 'Classe'])
    db=pd.concat([db, new_df], ignore_index=True)
    return db

def main():    
    df=pd.read_excel('path/to/excel/file')
    df_cedula_credito=df[df['Classe']=='cedula']
    df_certificado=df[df['Classe']=='certificado']
    df_comprovante=df[df['Classe']=='comprovante']
    df_proposta=df[df['Classe']=='detalhes']
    df_fatura=df[df['Classe']=='fatura']
    df_laudo_agressor=df[df['Classe']=='laudo1']
    df_laudo_atendimento=df[df['Classe']=='laudo2']
    df_laudo_checklist=df[df['Classe']=='laudo3']
    df_planilha=df[df['Classe']=='planilha']
    df_termo_adesao=df[df['Classe']=='termo']
    df_termo_consentimento=df[df['Classe']=='termo_consentimento']
    

    classes=[df_cedula_credito,df_certificado,df_comprovante,df_proposta,df_fatura,df_laudo_agressor,df_laudo_atendimento,df_laudo_checklist,df_planilha,df_termo_adesao,df_termo_consentimento]
    new_classes=[]

    for classe in classes:
        if len(classe)>100:
            new_classes.append(reduz_linhas(classe))

        elif len(classe)<100:
            nova_db=augment_data(classe)
            new_classes.append(nova_db)
            

        else:
            new_classes.append(classe)
    
    base_nova=pd.concat(new_classes)
    base_nova.to_excel('path/to/output.xlsx', index=False)

main()
