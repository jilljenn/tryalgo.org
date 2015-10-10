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
        if 0 <= i && i < n && 0 <= j && j < m && laby.(i).(j) = '.' then (
            laby.(i).(j) <- 'x';
            for dir = 0 to Array.length dirs - 1 do
                let di, dj = dirs.(dir) in
                explore (i + di) (j + dj)
            done
        )
    in explore 1 0;
    laby.(n - 1).(m - 2) = 'x'

let chemin n m laby =
    let dirs = [|(1, 0); (0, 1); (-1, 0); (0, -1)|] in
    let deja_vu = Array.init n (fun _ -> Array.init m (fun _ -> false)) in
    let prec = Array.init n (fun _ -> Array.init m (fun _ -> None)) in
    let rec explore todo = match todo with
        | [] -> ()
        | (i, j, p)::rest_todo -> (
            if 0 <= i && i < n && 0 <= j && j < m && laby.(i).(j) = '.' && not deja_vu.(i).(j) then (
                deja_vu.(i).(j) <- true;
                prec.(i).(j) <- p;
                if (i, j) = (n - 1, m - 2) then (); (* Cette ligne est facultative *)
                let rest_todo = Array.fold_left (fun t (di, dj) -> (i + di, j + dj, Some (i, j))::t) rest_todo dirs in
                explore rest_todo;
            ) else explore rest_todo
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
            if (i, j) = (n - 1, m - 2) then (); (* Cette ligne est facultative *)
            let rest_todo = Array.fold_left (fun t (di, dj) ->
                let ni = i + di and nj = j + dj in
                if 0 <= ni && ni < n && 0 <= nj && nj < m && laby.(ni).(nj) = '.' && not deja_vu.(ni).(nj) then (
                    deja_vu.(ni).(nj) <- true;
                    prec.(ni).(nj) <- Some (i, j);
                    enfile t (ni, nj)
                ) else
                    t) rest_todo dirs in
            explore rest_todo;
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
