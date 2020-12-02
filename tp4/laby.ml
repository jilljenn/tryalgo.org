(* Préliminaires, servez-vous ! *)

let affiche laby =
    for i = 0 to Array.length laby - 1 do
        Array.iter print_char laby.(i);
        print_newline ()
    done

let reconstruit n m laby prec =
    let rec parcourt i j =
        laby.(i).(j) <- 'x';
        match prec.(i).(j) with
            | None -> ()
            | Some (i, j) -> parcourt i j
    in parcourt (n - 1) (m - 2);
    affiche laby

type 'a type_file = {mutable tete: 'a list; mutable queue: 'a list}

let init_file () =
    {tete = []; queue = []}

let est_vide file =
    file.tete = [] && file.queue = []

let rec defile file =
    if est_vide file then failwith "La file est vide";
    match file.tete with
        | [] -> defile {tete = List.rev file.queue; queue = []}
        | h::t -> h, {tete = t; queue = file.queue}

let enfile file e =
    {tete = file.tete; queue = e::file.queue}

(* Votre mission commence ici *)

let sortie_accessible n m laby =
    let dirs = [|(1, 0); (0, 1); (-1, 0); (0, -1)|] in
    let rec explore i j =
        () (* Remplissez ici *)






    in explore 1 0;
    laby.(n - 1).(m - 2) = 'x'

let chemin n m laby =
    let dirs = [|(1, 0); (0, 1); (-1, 0); (0, -1)|] in
    let deja_vu = Array.init n (fun _ -> Array.init m (fun _ -> false)) in
    let prec = Array.init n (fun _ -> Array.init m (fun _ -> None)) in
    let rec explore todo = match todo with
        | [] -> ()
        | (i, j, p)::rest_todo -> (
            (* Remplissez ici *)






        )
    in explore [(1, 0, None)];
    reconstruit n m laby prec

let plus_court_chemin n m laby =
    let dirs = [|(1, 0); (0, 1); (-1, 0); (0, -1)|] in
    let deja_vu = Array.init n (fun _ -> Array.init m (fun _ -> false)) in
    let prec = Array.init n (fun _ -> Array.init m (fun _ -> None)) in
    let rec explore todo =
        if not (est_vide todo) then
            let (i, j), rest_todo = defile todo in
            () (* Remplissez ici *)









    in deja_vu.(1).(0) <- true;
    explore (enfile (init_file ()) (1, 0));
    reconstruit n m laby prec

(* Lecture de l'entrée *)

let _ =
    let n, m = Scanf.scanf "%d %d\n" (fun x y -> x, y) in
    let laby = Array.init n (fun _ ->
        let s = Scanf.scanf "%s\n" (fun x -> x) in
            Array.init m (fun n -> s.[n])
    ) in
    if sortie_accessible n m laby then print_string "OUI\n" else print_string "NON\n";
    (* chemin n m laby *)
    (* plus_court_chemin n m laby *)
