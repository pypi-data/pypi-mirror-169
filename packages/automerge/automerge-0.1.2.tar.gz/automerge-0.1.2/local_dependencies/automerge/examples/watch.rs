use automerge::transaction::CommitOptions;
use automerge::transaction::Transactable;
use automerge::Automerge;
use automerge::AutomergeError;
use automerge::Patch;
use automerge::VecOpObserver;
use automerge::ROOT;

fn main() {
    let mut doc = Automerge::new();

    let mut observer = VecOpObserver::default();
    // a simple scalar change in the root object
    doc.transact_with::<_, _, AutomergeError, _, _>(
        |_result| CommitOptions::default().with_op_observer(&mut observer),
        |tx| {
            tx.put(ROOT, "hello", "world").unwrap();
            Ok(())
        },
    )
    .unwrap();
    get_changes(&doc, observer.take_patches());

    let mut tx = doc.transaction();
    let map = tx
        .put_object(ROOT, "my new map", automerge::ObjType::Map)
        .unwrap();
    tx.put(&map, "blah", 1).unwrap();
    tx.put(&map, "blah2", 1).unwrap();
    let list = tx
        .put_object(&map, "my list", automerge::ObjType::List)
        .unwrap();
    tx.insert(&list, 0, "yay").unwrap();
    let m = tx.insert_object(&list, 0, automerge::ObjType::Map).unwrap();
    tx.put(&m, "hi", 2).unwrap();
    tx.insert(&list, 1, "woo").unwrap();
    let m = tx.insert_object(&list, 2, automerge::ObjType::Map).unwrap();
    tx.put(&m, "hi", 2).unwrap();
    let _heads3 = tx.commit_with(CommitOptions::default().with_op_observer(&mut observer));
    get_changes(&doc, observer.take_patches());
}

fn get_changes(doc: &Automerge, patches: Vec<Patch>) {
    for patch in patches {
        match patch {
            Patch::Put {
                obj,
                key,
                value,
                conflict: _,
            } => {
                println!(
                    "put {:?} at {:?} in obj {:?}, object path {:?}",
                    value,
                    key,
                    obj,
                    doc.path_to_object(&obj)
                )
            }
            Patch::Insert { obj, index, value } => {
                println!(
                    "insert {:?} at {:?} in obj {:?}, object path {:?}",
                    value,
                    index,
                    obj,
                    doc.path_to_object(&obj)
                )
            }
            Patch::Increment { obj, key, value } => {
                println!(
                    "increment {:?} in obj {:?} by {:?}, object path {:?}",
                    key,
                    obj,
                    value,
                    doc.path_to_object(&obj)
                )
            }
            Patch::Delete { obj, key } => println!(
                "delete {:?} in obj {:?}, object path {:?}",
                key,
                obj,
                doc.path_to_object(&obj)
            ),
        }
    }
}
