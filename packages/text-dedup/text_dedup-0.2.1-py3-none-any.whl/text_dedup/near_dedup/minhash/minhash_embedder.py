#!/usr/bin/env python
# @Date    : 2022-04-02 10:53:30
# @Author  : Chenghao Mou (mouchenghao@gmail.com)
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
from typing import List
from typing import Sequence

from datasketch import MinHash

from text_dedup.base import Embedder
from text_dedup.base import Fingerprint
from text_dedup.preprocess import tokenize


@dataclass
class MinHashEmbedder(Embedder):
    """
    Old but gold MinHash. This is basically a wrapper around the datasketch library.

    Parameters
    ----------
    num_perm : int, optional (default=128)
        Number of permutations to use.
    seed : int, optional (default=42)
        Seed for the random number generator and permutation.
    tokenizer : Callable, optional (default=tokenize)
        Tokenizer function.

    Examples
    --------
    >>> from text_dedup.near_dedup.minhash import MinHashEmbedder
    >>> embedder = MinHashEmbedder(128)
    """

    num_perm: int = 128
    seed: int = 42
    tokenizer: Callable[..., List[str]] = tokenize

    def embed(self, corpus: Sequence[str], **kwargs) -> List[Fingerprint]:
        """
        Embed a list of strings. It applies the embedding function to each string sequentially.
        It is recommended to use the `embed_function` method instead, in parallel, for example.

        Parameters
        ----------
        corpus : List[str]
            List of strings to embed.
        kwargs : dict
            Additional keyword arguments for tokenization.

        Returns
        -------
        List[Fingerprint]
            Embeddings of the corpus.

        Examples
        --------
        >>> from text_dedup.near_dedup.minhash import MinHashEmbedder
        >>> embedder = MinHashEmbedder(128)
        >>> embeddings = embedder.embed(["hello world", "hello world"])
        >>> len(embeddings)
        2
        """
        f = self.embed_function(**kwargs)
        return [f(doc) for doc in corpus]

    def embed_function(self, **kwargs) -> Callable[[str], Fingerprint]:
        """
        Embedding function that takes a string and returns the embedding/fingerprint.

        Parameters
        ----------
        kwargs : dict
            Additional keyword arguments for tokenization.

        Returns
        -------
        Callable[[str], Fingerprint]
            Embedding function.

        Examples
        --------
        >>> from text_dedup.near_dedup.minhash import MinHashEmbedder
        >>> embedder = MinHashEmbedder(128)
        >>> hashes = embedder.embed_function()("hello world")
        >>> hashes.shape
        (128,)
        """
        def wrapper(doc: str) -> Fingerprint:
            m: MinHash = MinHash(num_perm=self.num_perm, seed=self.seed)
            tokens = self.tokenizer(doc, **kwargs)
            m.update_batch([token.encode("utf-8") for token in tokens])
            return m.hashvalues

        return wrapper

    def __repr__(self) -> str:
        return f"MinHashEmbedder(num_perm={self.num_perm}, seed={self.seed}, tokenizer={self.tokenizer.__name__})"
