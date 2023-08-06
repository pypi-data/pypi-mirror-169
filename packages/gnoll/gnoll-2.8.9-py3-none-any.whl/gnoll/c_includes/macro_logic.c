
#include "uthash.h"
#include "vector_functions.h"
#include "macro_logic.h"

struct macro_struct *macros = NULL; //Initialized to NULL (Importnat)


void register_macro(char * skey, vec *to_store) {
    int key = atoi(skey);
    struct macro_struct *s;

    HASH_FIND_INT(macros, &key, s);  /* id already in the hash? */
    if (s == NULL){
        s = (struct macro_struct*)malloc(sizeof *s);
        s->id = key;
        HASH_ADD_INT(macros, id, s);  /* id: name of key field */
    }
    memcpy(&s->stored_dice_roll, &to_store, sizeof(*to_store));
}

struct macro_struct *search_macros(char * skey, vec *to_store) {
    int key = atoi(skey);
    struct macro_struct *s;

    HASH_FIND_INT(macros, &key, s);  /* s: output pointer */
    return s;
}